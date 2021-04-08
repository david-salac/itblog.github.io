# New Python library for exporting formulas to Excel and other formats
import datetime
import crinita as cr

lead = """One of the typical challenges when doing the export of numerical computations is how to include the way your computations were achieved. Typically, if results should be in an Excel sheet in the end, you want to see a computation formula if you click on each cell. There is a native method - using some Excel driver (like XlsxWriter) available in Python."""

content = """One of the typical challenges when doing the export of numerical computations is how to include the way your computations were achieved. Typically, if results should be in an Excel sheet in the end, you want to see a computation formula if you click on each cell. There is a native method - using some Excel driver (like XlsxWriter) available in Python. But if you are dealing with a big Excel sheet (or multiple sheets in one file), this approach becomes quite inconvenient. We present a new library called Portable Spreadsheet - it can easily export simply defined formulas in Python to many formats including Excel, JSON, etc.
<h2>Simple problem</h2>
<p>Say that you have an e-shop written in Python and want to export some simple Excel sheet that summarizes revenues per each category. There can be just two columns, one representing the category and another one representing revenues. </p> 

<figure>
<img alt="Excel" src="images/excel.png">
<figcaption>Simple problem definition</figcaption>
</figure>

<p>In the end, you want to see some aggregation functions, like the sum of all revenues, the article with minimal revenue, and say the sum of food and drinks as a new category (called grocery). What is crucial, the spreadsheet should be editable, it means, each computation should be exported as a formula (as illustrated in the figure above).</p>
<h2>Approach using available Excel drivers</h2>
<p>You can tackle this issue directly using some driver for Excel available in Python. Let's say you choose XlsxWriter as your driver. Then you have to define each cell value and for the computations the way how you compute it plus the actual value after the computation. The code you have to write would follow the logic:</p>
<pre class="code"><code>import xlsxwriter
workbook = xlsxwriter.Workbook('revenues.xlsx')
worksheet = workbook.add_worksheet()
food_rev = 1000
drinks_rev = 100
headphones_rev = 300
# Write categories
worksheet.write(0, 0, "Food")
worksheet.write(1, 0, "Drinks")
worksheet.write(2, 0, "Headphones")
# Write revenues
worksheet.write(0, 1, food_rev)
worksheet.write(1, 1, drinks_rev)
worksheet.write(2, 1, headphones_rev)
# Write results
worksheet.write_formula(
    3, 1, "=SUM(B1:B3)", 
    value=(food_rev + drinks_rev + headphones_rev)
)
worksheet.write_formula(
    4, 1, "=MIN(B1:B3)",
    value=min(food_rev, drinks_rev, headphones_rev)
)
worksheet.write_formula(5, 1, "=B1+B2",
                        value=food_rev + drinks_rev)
# Close the sheet (in order to write it to the file)
workbook.close()
</code></pre>

<p>As you can see the code is not simple (nor complete) and you already had to hardwire the positions of each cell in it. You also had to use values for computations multiple times as you cannot directly use the values in the cell.</p>
<p>What more is that when you decide to export to the different format (say JSON), you have to write this code again.</p>
<h2>Portable Spreadsheet approach</h2>
<p>Another way how to deal with all these issues elegantly is to use a library called Portable Spreadsheet (installable easily via pip install portable-spreadsheet). Consider the following code as the opposite of the previous one:</p>

<pre class="code"><code>import portable_spreadsheet as ps

# Create the spreadsheet with the correct labels
sheet = ps.Sheet.create_new_sheet(
    6, 1,
    rows_labels=['Food', 'Drink', 'Headphones', 'Total', 'Minimal', 'Grocery'],
    columns_labels=['Revenue']
)
# Set the values (in the Pandas-like way)
sheet.loc['Food', 'Revenue'] = 15000
sheet.loc['Drink', 'Revenue'] = 16000
sheet.loc['Headphones', 'Revenue'] = 1000
# Set the computations
sheet.loc['Total', 'Revenue'] = \
    sheet.loc['Food':'Total', 'Revenue'].sum()
sheet.loc['Minimal', 'Revenue'] = \ 
    sheet.loc['Food':'Total', 'Revenue'].min()
sheet.loc['Grocery', 'Revenue'] = (
        sheet.loc['Food', 'Revenue'] + 
        sheet.loc['Drink', 'Revenue']
    )
# Export result to Excel
sheet.to_excel("rev.xlsx")
# Export result to JSON
json = sheet.to_json()</code></pre>


<p>As you can see, you completely removed redundancies in the code, it is shorter, easily readable, and what's best, you can export not only to Excel but to every reasonable format (JSON, CSV, HTML, etc.). If you are familiar with Pandas DataFrame concept, you can see the straight motivation.</p>
<h3>How does it work under the hood?</h3>
<p>Internally, the principle of the Portable Spreadsheet library lies in the word constructing algorithm. Basically, each formula (in Excel, JSON, etc.) can be considered as a world in some language. This language is the Context-Free language defined by Context-Free grammar (see Chomsky hierarchy).</p>
<p>This practically means that all that is needed is the definition of the prefixes and suffices for each operation. Operands here are the coordinates of the cells.</p>
<p>So, if you want to compute the sum of the items in the column, your operands are the coordinates of slice start and end, the operation is the sum (you have two inputs: operation and operands).</p>

<figure>
<img alt="Prefixes and suffixes of operation and operands" src="images/pref_suf.png">
<figcaption>Prefixes and suffixes of operation and operands</figcaption>
</figure>

<p>In the picture above, you can see prefixes and suffixes. Some prefixes and suffixes are empty sets. This picture is just an illustration, but it shows how each word can be constructed. All these prefixes and suffixes (and other rules) are defined as the grammars for each language in a separate file.</p>
<p>The rest of the Portable Spreadsheet library is simple storing of words for each cell defined by its coordinates. Each word (like that one with the sum mentioned above) can be the part of the other word (acting as an operand). This approach allows defining grammars for each language that should be part of the export (like native language description, Python language, Excel).</p>

<h2>The new version of Portable Spreadsheet</h2>
<p>There is also a new version of Portable Spreadsheet now available. It contains many enhanced features (like the possibility of speed optimization). But the main new feature is the support of outputs with multiple sheets - called Workbook. The interface for using the workbook is very intuitive - it is a container for sheets (with implemented functionality for exporting). Another enhancement is the possibility to have a custom-defined variables sheet - that is a sheet that defines variables for computations in other sheets (you can add as many columns and rows as needed with your content).</p> 
<p>Regarding performance, the most important new feature enables you to create a sheet with values only (it means, you cannot export to Excel/JSON and other formats afterwards). That makes computations much faster. You just need to recompute all the values with proper configuration when you need them. Also, there is now a possibility to reduce the number of languages in which words are constructed - so for example, if you want to export only to Excel, you do not need to waste your computational time with other formats (this feature makes library slightly faster as well). </p>
<p>Alas, the only way how to improve the Portable Spreadsheet library was to use an application interface that is not backwards compatible in a few ways (for example, Spreadsheet class was renamed to Sheet). There are also many new classes available (that allows the creation of outputs with multiple sheets in them). Many bugs were fixed as well (like the bug in shape property that now works correctly).</p>

<h2>Summary </h2>
<p>The purpose of this article is to present a new library for Python called Portable Spreadsheet (pip install portable-spreadsheet) that allows you to easily export computation formulas in a spreadsheet to various type of formats (mainly Excel and JSON). So you can see how each computation in a spreadsheet is done without manually coding each cell. </p>
"""

ENTITY = cr.Article(
    title="New Python library for exporting formulas to Excel and other formats",
    url_alias='new-python-library-for-exporting-formulas-to-excel-and-other-formats',
    large_image_path="images/portable_spreadsheet_big.jpg",
    small_image_path="images/portable_spreadsheet_small.jpg",
    date=datetime.datetime(2020, 8, 16),
    tags=[cr.Tag('Data Visualisation', 'data-visualisation'),
          cr.Tag('Exporting', 'exporting'),
          cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Excel', 'excel')],
    content=content,
    lead=lead,
    description="We present a new library called Portable Spreadsheet - it can easily export simply defined formulas in Python to many formats including Excel, JSON, etc."  # noqa: E501
)
