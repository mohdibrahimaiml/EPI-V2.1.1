"""Convert EPI founder's report from Markdown to PDF."""
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Source and destination paths
md_file = Path(r"C:\Users\dell\.gemini\antigravity\brain\9dcbc419-273b-423e-93f9-af66ae181f77\epi_founder_complete_report.md")
pdf_file = Path(r"C:\Users\dell\.gemini\antigravity\brain\9dcbc419-273b-423e-93f9-af66ae181f77\epi_founder_complete_report.pdf")

# Read markdown
md_content = md_file.read_text(encoding='utf-8')

# Convert markdown to HTML with extensions
html_content = markdown.markdown(
    md_content,
    extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists']
)

# Add CSS styling for professional PDF
css = CSS(string='''
    @page {
        size: A4;
        margin: 2cm;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 9pt;
            color: #666;
        }
    }
    body {
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
    }
    h1 {
        color: #1a1a1a;
        font-size: 24pt;
        margin-top: 20pt;
        margin-bottom: 12pt;
        border-bottom: 2px solid #0066cc;
        padding-bottom: 6pt;
    }
    h2 {
        color: #0066cc;
        font-size: 18pt;
        margin-top: 16pt;
        margin-bottom: 10pt;
    }
    h3 {
        color: #333;
        font-size: 14pt;
        margin-top: 12pt;
        margin-bottom: 8pt;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: "Consolas", monospace;
        font-size: 10pt;
    }
    pre {
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 12px;
        overflow-x: auto;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 12pt 0;
    }
    th {
        background-color: #0066cc;
        color: white;
        padding: 8px;
        text-align: left;
        font-weight: bold;
    }
    td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    blockquote {
        border-left: 4px solid #0066cc;
        padding-left: 16px;
        margin-left: 0;
        color: #666;
        font-style: italic;
    }
    ul, ol {
        margin-left: 20pt;
    }
''')

# Wrap HTML with proper structure
full_html = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>EPI Founder's Complete Report</title>
</head>
<body>
    {html_content}
</body>
</html>
'''

# Generate PDF
print("Converting markdown to PDF...")
HTML(string=full_html).write_pdf(pdf_file, stylesheets=[css])
print(f"✅ PDF created: {pdf_file}")
print(f"📄 File size: {pdf_file.stat().st_size / 1024:.1f} KB")
