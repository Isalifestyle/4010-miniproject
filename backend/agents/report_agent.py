from fpdf import FPDF
import uuid
import os

def generate_pdf(topic, analysis):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    filename = f"{reports_dir}/report_{uuid.uuid4()}.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Research Report: {topic}", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=analysis)
    pdf.output(filename)
    return filename
