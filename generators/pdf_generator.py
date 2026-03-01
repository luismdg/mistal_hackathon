from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from domain.model_state import model_state

def generate_pdf(path="output.pdf"):
    doc = SimpleDocTemplate(path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("User Stories", styles["Heading1"]))
    elements.append(Spacer(1, 12))

    for story in model_state.user_stories:
        elements.append(Paragraph(story, styles["Normal"]))
        elements.append(Spacer(1, 12))

    doc.build(elements)

    return path