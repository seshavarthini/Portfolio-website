from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import TA_CENTER

def generate_resume(data):

    pdf = SimpleDocTemplate("resume.pdf")

    styles = getSampleStyleSheet()

    content = []

    about = data["about"]

    name_style = ParagraphStyle(

    "Name",

    parent=styles["Title"],

    fontSize=30,

    leading=34,

    alignment=TA_CENTER

    )

    title_style = ParagraphStyle(
       "Title",
       parent=styles["BodyText"],
       fontSize=16,
       alignment=TA_CENTER
    )

    contact_style = ParagraphStyle(
       "Contact",
       parent=styles["BodyText"],
       fontSize=10,
       alignment=TA_CENTER
    )

    section_style = ParagraphStyle(
       "Section",
       parent=styles["Heading2"],
       fontSize=14
    )

    content_style = ParagraphStyle(
       "Content",
       parent=styles["BodyText"],
       fontSize=11
    )
    # Name
    content.append(
       Paragraph(
          about["name"],
          name_style
        )
    )
    #title
    content.append(
        Paragraph(
          about["title"],
          title_style
        )
    )
    # Contact

    contact = f"""
    Email: {about['email']}<br/>
    Phone: {about['phone']}<br/>
    GitHub: {about['github']}<br/>
    LinkedIn: {about['linkedin']}
    """

    content.append(
        Paragraph(
            contact,
            contact_style
        )
    )

    content.append(Spacer(1, 12))

    # Line

    content.append(
        HRFlowable(
          width="100%",
          thickness=1
        )
    )

    # Objective

    # OBJECTIVE

    content.append(HRFlowable(width="100%", thickness=1))

    content.append(
        Paragraph(
          "CAREER OBJECTIVE",
          section_style
        )
    )

    content.append(
        Paragraph(
          data["objective"],
          content_style
        )
    )
    
    # EDUCATION

    content.append(HRFlowable(width="100%", thickness=1))

    content.append(
        Paragraph(
          "EDUCATION",
          section_style
        )
    )

    for edu in data["education"]:

        content.append(
            Paragraph(
              edu["title"],
              content_style
            )
        )

# education content here

    # Skills
    content.append(HRFlowable(width="100%", thickness=1))
    content.append(
        Paragraph(
            "SKILLS",
            section_style
        )
    )

    for skill in data["skills"]:

        content.append(
            Paragraph(
                f"• {skill}",
                content_style
            )
        )

    content.append(HRFlowable(width="100%", thickness=1))
    content.append(
        Paragraph(
          "PROJECTS",
          section_style
        )
    )

# 👇 Idhu dhaan section content

    for project in data["projects"]:

        content.append(
            Paragraph(
              project["title"],
              content_style
            )
        )

        content.append(
            Paragraph(
              project["description"],
              content_style
            )
        )

    content.append(HRFlowable(width="100%", thickness=1))

    content.append(
         Paragraph(
          "ACHIEVEMENTS",
          section_style
        )
    )

    for achievement in data["achievements"]:

        content.append(
            Paragraph(
              f"• {achievement['title']}",
              content_style
            )
        )

    content.append(HRFlowable(width="100%", thickness=1))

    content.append(
        Paragraph(
          "CERTIFICATIONS",
          section_style
        )
    )

    for cert in data["certifications"]:

        content.append(
            Paragraph(
              f"• {cert['title']}",
              content_style
            )
        )
    content.append(HRFlowable(width="100%", thickness=1))

    content.append(
        Paragraph(
          "PUBLICATIONS",
          section_style
        )
    )

    for pub in data["publications"]:

        content.append(
            Paragraph(
              pub["title"],
              content_style
            )
        )

        content.append(
            Paragraph(
              pub["description"],
              content_style
            )
        )

    pdf.build(content)

    return "resume.pdf"