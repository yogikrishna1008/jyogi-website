from __future__ import annotations

from typing import Iterable, Tuple, Optional, List
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

Section = Tuple[str, str]

def _p(text: str) -> str:
    if text is None:
        return ""
    s = escape(str(text))
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    return s.replace("\n", "<br/>")

def save_reading_to_pdf(filename: str, sections: Iterable[Section], title: Optional[str] = None) -> bool:
    try:
        styles = getSampleStyleSheet()
        body = ParagraphStyle("body", parent=styles["BodyText"], fontSize=11, leading=14)
        h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontSize=18, leading=22, spaceAfter=10)
        h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=13, leading=16, spaceBefore=10, spaceAfter=6)

        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            leftMargin=0.75 * inch,
            rightMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
            title=title or "Jyogi Report",
            author="Jyogi",
        )

        story: List = []
        story.append(Paragraph(_p(title or "Jyogi Report"), h1))
        story.append(Paragraph(_p("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M")), body))
        story.append(Spacer(1, 12))

        first = True
        for heading, text in list(sections):
            if not first:
                story.append(PageBreak())
            first = False
            story.append(Paragraph(_p(heading), h2))
            story.append(Paragraph(_p(text), body))

        doc.build(story)
        return True
    except Exception as e:
        print("[pdf_writer] error:", e)
        return False
