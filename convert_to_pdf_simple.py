"""Convert EPI founder's report from Markdown to PDF using markdown2pdf."""
from pathlib import Path
import subprocess

# Source and destination paths
md_file = Path(r"C:\Users\dell\.gemini\antigravity\brain\9dcbc419-273b-423e-93f9-af66ae181f77\epi_founder_complete_report.md")
pdf_file = Path(r"C:\Users\dell\.gemini\antigravity\brain\9dcbc419-273b-423e-93f9-af66ae181f77\epi_founder_complete_report.pdf")

print("Converting markdown to PDF using markdown-pdf...")
print(f"Source: {md_file}")
print(f"Output: {pdf_file}")

# Try using markdown-pdf (npm package) if available
try:
    result = subprocess.run(
        ['markdown-pdf', str(md_file), '-o', str(pdf_file)],
        capture_output=True,
        text=True,
        timeout=60
    )
    if result.returncode == 0:
        print(f"✅ PDF created successfully!")
        print(f"📄 Location: {pdf_file}")
    else:
        print(f"❌ Conversion failed: {result.stderr}")
        print("\n🔧 Trying alternative method...")
        raise Exception("markdown-pdf not available")
except (FileNotFoundError, subprocess.TimeoutExpired, Exception) as e:
    # Alternative: Use Python's reportlab
    print("Using Python reportlab for PDF generation...")
    
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    import re
    
    # Read markdown
    content = md_file.read_text(encoding='utf-8')
    
    # Create PDF
    doc = SimpleDocTemplate(
        str(pdf_file),
        pagesize=A4,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch
    )
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor='#0066cc',
        spaceAfter=12,
        alignment=TA_CENTER
    )
    heading1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=16,
        textColor='#0066cc',
        spaceAfter=10,
        spaceBefore=12
    )
    heading2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#333',
        spaceAfter=8,
        spaceBefore=10
    )
    
    # Build content
    story = []
    
    # Add title
    story.append(Paragraph("EPI FOUNDER'S COMPLETE REPORT", title_style))
    story.append(Paragraph("Everything You Need to Know About EPI-Recorder", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Process markdown (simple conversion)
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        
        if not line:
            story.append(Spacer(1, 0.1*inch))
            continue
        
        # Headers
        if line.startswith('# ') and not line.startswith('## '):
            text = line[2:].replace('#', '')
            story.append(Paragraph(text, heading1_style))
        elif line.startswith('## '):
            text = line[3:].replace('#', '')
            story.append(Paragraph(text, heading2_style))
        elif line.startswith('### '):
            text = line[4:].replace('#', '')
            story.append(Paragraph(text, styles['Heading3']))
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            text = '• ' + line[2:]
            story.append(Paragraph(text, styles['Normal']))
        # Code blocks (ignore)
        elif line.startswith('```'):
            continue
        # Regular text
        elif not line.startswith('---'):
            # Clean markdown formatting
            text = line.replace('**', '<b>').replace('**', '</b>')
            text = text.replace('`', '<font face="courier">')
            text = text.replace('`', '</font>')
            story.append(Paragraph(text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF created successfully using reportlab!")
    print(f"📄 Location: {pdf_file}")
    print(f"📊 File size: {pdf_file.stat().st_size / 1024:.1f} KB")
