from lxml import etree
from io import StringIO


from latex_config import LaTeXConfig


def find_all(search_for: str, where: str) -> list[int]:
    """Find all ocurences of substring in the string
    Args:
        search_for (str): Text that is searched in where argument.
        where (str): The body of text where substring is searched.
    Returns:
        list[int]: List of indices with positions
    """
    positions: list[int] = []
    start_pos: int = 0
    while True:
        next_pos = where.find(search_for, start_pos)
        if next_pos > -1:
            start_pos = next_pos + 1
            positions.append(next_pos)
        else:
            break
    return positions


def tex_cleaning(html_code: str) -> tuple[str, list[str]]:
    """Cleaning work before converting tags to TeX.
    Notes:
        - Replace underscores with '\_'
        - Replace sharp symbol with '\#'
        - Does not do these replacements (above) in code block.
        - Replace <pre class="code"><code> -> <code-block>
        - Replace </code></pre> -> </code-block>
        - Replace quotation mark ' -> \text{\textquotesingle}
        - Replace double quotation mark " -> \text{\textquotedblright}
        - Does not do last two replacement in code block.
    Returns:
        tuple[str, list[str]]: Cleaned string and tuple of code blocks.
    """
    # Cleaning
    html = html_code.replace('<pre class="code"><code>', '<code-block>')
    html = html.replace('</code></pre>', '</code-block>')
    html = html.replace("<!-- LATEX ", '<latex-code>')
    html = html.replace(" LATEX -->", '</latex-code>')
    # Change GIF to PNG
    html = html.replace(".gif", '.png')

    # Parse all em blocks as italic text:
    if "<!-- LATEX-ALL-EM-AS-TEXT -->" in html:
        html = html.replace("<em>", '<em class="text">')
        html = html.replace("<!-- LATEX-ALL-EM-AS-TEXT -->", "")

    # Filter code blocks:
    code_blocks: list[str] = []
    for st, en in zip(find_all('<code-block>', html),
                      find_all('</code-block>', html)):
        code_block = html[st + len("<code-block>"):en]
        code_block = code_block.replace('$', '\\$')
        code_blocks.append(code_block)
    # Replace underscore
    html = html.replace('_', '\\_')
    html = html.replace('#', '\\#')
    html = html.replace('£', '\\text{\\pounds}')

    # Quotation marks
    new_htmls = []
    prev_st = 0
    for st, en in zip(find_all('<code>', html),
                      find_all('</code>', html)):
        en += len("</code>")
        new_htmls.append(html[prev_st:st])
        block = html[st:en]
        block = block.replace(r"'", r'\text{\textquotesingle}')
        block = block.replace(r'"', r'\text{\textquotedblright}')
        new_htmls.append(block)
        prev_st = en
    # Add remainder
    new_htmls.append(html[prev_st:])
    html = "".join(new_htmls)

    # Backslash before underscore
    new_htmls = []
    prev_st = 0
    for st, en in zip(find_all('<latex-code>', html),
                      find_all('</latex-code>', html)):
        en += len("</latex-code>")
        new_htmls.append(html[prev_st:st])
        block = html[st:en]
        block = block.replace("\\_", r'_')
        new_htmls.append(block)
        prev_st = en
    # Add remainder
    new_htmls.append(html[prev_st:])
    html = "".join(new_htmls)

    return html, code_blocks


class CodeBlocksManagement:
    """Static class that contains all code blocks and the pointer to the
    last used block.
    """
    code_blocks: list[str] = []
    code_block_position: int = 0


def html2latex(html_code: str) -> str:
    """Convert HTML to TeX format."""
    result = []
    if html_code.text:
        result.append(html_code.text)
    for sel in html_code:
        # print('tag', sel.tag)
        # print('text', sel.text)
        # print('tail', sel.tail)
        # print('attrib', sel.attrib)

        # Skip in the case of 'math' class
        if 'class' in sel.attrib.keys():
            if 'math' in sel.attrib['class']:
                continue
        match sel.tag:
            case 'h1':
                result.append('\hmchapter{%s}' % html2latex(sel))
            case 'h2':
                result.append('\\section{%s}' % html2latex(sel))
            case 'h3':
                result.append('\\subsection{%s}' % html2latex(sel))
            case 'h4':
                result.append('\\subsubsection{%s}' % html2latex(sel))
            case 'code':
                result.append('\\texttt{%s}' % html2latex(sel))
            case 'p':
                result.append('\n%s\n' % html2latex(sel))
            case "code-block":
                # Here does not do any further interpretation
                result.append(
                    '\\begin{Verbatim}[fontsize=\\normalsize]\n%s\n\\end{Verbatim}\n' % CodeBlocksManagement.code_blocks[CodeBlocksManagement.code_block_position]
                )
                CodeBlocksManagement.code_block_position += 1
            case "ol":
                result.append('\\begin{enumerate}\n%s\n\\end{enumerate}\n' % html2latex(sel))
            case "ul":
                result.append('\\begin{itemize}\n%s\n\\end{itemize}\n' % html2latex(sel))
            case "li":
                result.append('\\item %s\n' % html2latex(sel))
            case "doc-title":
                result.append('\\begin{flushleft}\\textbf{\LARGE\n\\raggedright %s }\\end{flushleft}\n\n' % html2latex(sel))
            case "figure":
                result.append('\\begin{figure}[h]\n%s\n\\end{figure}\n' % html2latex(sel))
            case "img":
                # Center image and replace backslash before underscore in source
                result.append('\\centering\n\\includegraphics{%s}\n' % sel.attrib['src'].replace('\\', ''))
            case "figcaption":
                # Remove 'Figure NR: ' string:
                caption_text: str = str(sel.text)
                if caption_text.lower().startswith("figure"):
                    caption_text = caption_text[caption_text.find(':') + 2:]
                # Insert center-align caption
                result.append('\\caption{\\centering %s }\n' % caption_text)
            case "latex-code":
                result.append(sel.text)
            case "em" if 'class' in sel.attrib.keys() and 'text' in sel.attrib['class']:
                result.append('\\textit{%s}' % html2latex(sel))
            case "em" if 'class' in sel.attrib.keys() and 'equation' in sel.attrib['class']:
                result.append('${%s}$' % html2latex(sel))
            case "strong":
                result.append('\\textbf{%s}' % html2latex(sel))
            case "table":
                # Must have 'having-N-columns' attribute
                nr_columns: int = 0
                for _cls in str(sel.attrib['class']).split(' '):
                    if _cls.startswith('having-') and _cls.endswith('columns'):
                        nr_columns = int(
                            _cls[len('having-'):_cls.index('-columns')]
                        )
                t_def: str = "|".join(["c" for _ in range(nr_columns)])
                t_content = html2latex(sel)
                t_content = t_content.replace('\n& ', '\n')
                pattern = r"""\begin{center}
                \begin{tabular}{|""" + t_def + """|} 
                \hline
                  %s
                \end{tabular}
                \end{center}
                """ % t_content
                result.append(pattern)
            case "tr":
                processed_tds = html2latex(sel)
                pre_tds = ""
                for ln in processed_tds.splitlines():
                    pre_tds += ln.lstrip(' ')
                pre_tds = pre_tds.lstrip('& ')
                result.append(r'%s \\ \hline' % pre_tds)
            case "td":
                result.append(r'& %s' % html2latex(sel))
            case "th":
                result.append(r'& \textbf{%s}' % html2latex(sel))
            case "a":
                result.append(f'{html2latex(sel)} ({sel.attrib["href"]})')
            case _ if (sel.tag != "body"):
                raise Exception(f"Unknown tag '{sel.tag}', context: {sel.text}")
            case _:
                result.append(html2latex(sel))
        if sel.tail:
            result.append(sel.tail)
    return "".join(result)


def build_latex_doc(html: str, doc_title: str) -> str:
    """Create the whole document structure.
    """
    # Cleaning
    html, _code_blocks = tex_cleaning(html)
    CodeBlocksManagement.code_blocks = _code_blocks
    CodeBlocksManagement.code_block_position = 0

    # Parse
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html),
                       parser)  # expects a file, use StringIO for string
    root = tree.getroot()
    latex = html2latex(root)
    # Prepare docs
    docs_start: str = LaTeXConfig.DOCUMENT_START
    # Write results to file
    return "".join([docs_start,
                    '\\chapter{%s}\n' % doc_title,
                    latex,
                    LaTeXConfig.DOCUMENT_END])
