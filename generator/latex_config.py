from pathlib import Path


class LaTeXConfig:
    OUTPUT_DIRECTORY: Path = Path('../latex')
    DOCUMENT_START: str = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

% Formating:
% \usepackage{times}
\usepackage{fancyvrb}
% To include images
\usepackage{graphicx}
\usepackage{float}

% No word splitting:
\tolerance=1
\emergencystretch=\maxdimen
\hyphenpenalty=10000
\hbadness=10000

% Quotation marks
\usepackage{upquote}

% Chapter command
\newcommand{\chapter}[1]{\begin{flushleft}\textbf{\LARGE\raggedright #1 }\end{flushleft}} % version 1

\begin{document}

"""
    DOCUMENT_END: str = r"\end{document}"
