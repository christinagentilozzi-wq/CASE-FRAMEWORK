from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

file_path = "/mnt/data/UI_UX_Case_Study_Master_System_v1.pdf"

doc = SimpleDocTemplate(
    file_path,
    pagesize=LETTER,
    rightMargin=72,
    leftMargin=72,
    topMargin=72,
    bottomMargin=72,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleStyle", fontSize=22, spaceAfter=20, leading=26))
styles.add(ParagraphStyle(name="HeaderStyle", fontSize=16, spaceAfter=14, leading=20))
styles.add(ParagraphStyle(name="BodyStyle", fontSize=11, spaceAfter=10, leading=15))

story = []

story.append(Paragraph("UI/UX Case Study Master System", styles["TitleStyle"]))
story.append(Paragraph("Human-Centered · Research-Grounded · Design-Led", styles["BodyStyle"]))
story.append(Spacer(1, 0.4 * inch))

story.append(Paragraph("Badge Placeholder", styles["HeaderStyle"]))
story.append(Paragraph(
    "Reserved space for Tech Badge from Figma. This badge will be embedded here in future versions when exported as PNG or SVG.",
    styles["BodyStyle"],
))
story.append(PageBreak())

sections = [
    ("Master Prompt (v1)", "Foundational structured prompt for building UX case studies with ethical rigor and operational realism."),
    ("Master Prompt v2A — UX-Heavy Variant", "Design-forward variant prioritizing flows, wireframes, interaction, and usability."),
    ("Master Prompt v2B — Research-Heavy Variant", "Research-driven variant emphasizing systems thinking, analysis, and strategy."),
    ("Canva Master Template Specification", "Standardized slide structure, visual rules, and branding guidance."),
    ("Case Study Intake Checklist", "Pre-project checklist ensuring clarity, constraints, and focus before design begins."),
    ("Portfolio / GitHub README Attachment", "Reusable README block explaining the case study framework."),
    ("System Usage & Versioning Guide", "Instructions for maintaining, updating, and evolving the Master System over time."),
]

for title, desc in sections:
    story.append(Paragraph(title, styles["HeaderStyle"]))
    story.append(Paragraph(desc, styles["BodyStyle"]))
    story.append(Spacer(1, 0.25 * inch))

doc.build(story)

file_path
