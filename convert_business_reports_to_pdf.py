#!/usr/bin/env python3
"""Convert business_report Markdown reports to readable PDFs."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path("/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline")
REPORT_DIR = ROOT / "business_report"


def register_fonts() -> str:
    # Built-in CJK CID font keeps Chinese text readable without relying on
    # user-installed Python font packages.
    font_name = "STSong-Light"
    pdfmetrics.registerFont(UnicodeCIDFont(font_name))
    return font_name


def clean_inline(text: str) -> str:
    text = text.strip()
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    return text


def make_styles(font_name: str) -> dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "BaseCJK",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=9,
        leading=13,
        wordWrap="CJK",
        spaceAfter=3,
        textColor=colors.HexColor("#172033"),
    )
    return {
        "title": ParagraphStyle(
            "TitleCJK",
            parent=base,
            fontSize=18,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0F2E46"),
            spaceAfter=10,
        ),
        "h1": ParagraphStyle(
            "Heading1CJK",
            parent=base,
            fontSize=15,
            leading=20,
            textColor=colors.HexColor("#123B5D"),
            spaceBefore=10,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "Heading2CJK",
            parent=base,
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#174A6B"),
            spaceBefore=8,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "Heading3CJK",
            parent=base,
            fontSize=10,
            leading=14,
            textColor=colors.HexColor("#1F5F7A"),
            spaceBefore=6,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": base,
        "bullet": ParagraphStyle(
            "BulletCJK",
            parent=base,
            leftIndent=12,
            firstLineIndent=0,
            bulletIndent=2,
            spaceAfter=4,
        ),
        "quote": ParagraphStyle(
            "QuoteCJK",
            parent=base,
            leftIndent=10,
            rightIndent=8,
            textColor=colors.HexColor("#4A5568"),
            backColor=colors.HexColor("#F7FAFC"),
            borderColor=colors.HexColor("#CBD5E0"),
            borderWidth=0.5,
            borderPadding=5,
            spaceBefore=4,
            spaceAfter=6,
        ),
        "footer": ParagraphStyle(
            "FooterCJK",
            parent=base,
            fontSize=7,
            leading=9,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#718096"),
        ),
    }


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean_inline(text), style)


def markdown_to_story(markdown: str, styles: dict[str, ParagraphStyle]) -> list:
    story = []
    pending_para: list[str] = []

    def flush_para() -> None:
        if pending_para:
            story.append(paragraph(" ".join(pending_para), styles["body"]))
            pending_para.clear()

    lines = markdown.splitlines()
    first_heading = True
    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_para()
            story.append(Spacer(1, 2))
            continue

        if stripped == "---":
            flush_para()
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.45, color=colors.HexColor("#D8DEE9")))
            story.append(Spacer(1, 5))
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            flush_para()
            level = len(heading.group(1))
            text = heading.group(2)
            if level == 1 and first_heading:
                story.append(paragraph(text, styles["title"]))
                first_heading = False
            else:
                story.append(paragraph(text, styles.get(f"h{min(level, 3)}", styles["h3"])))
            continue

        if stripped.startswith(">"):
            flush_para()
            story.append(paragraph(stripped.lstrip("> "), styles["quote"]))
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        numbered = re.match(r"^\d+(?:\.\d+)?\.\s+(.+)$", stripped)
        if bullet or numbered:
            flush_para()
            item_text = bullet.group(1) if bullet else numbered.group(1)
            bullet_text = "-" if bullet else "•"
            story.append(
                ListFlowable(
                    [ListItem(paragraph(item_text, styles["bullet"]))],
                    bulletType="bullet",
                    start=bullet_text,
                    leftIndent=8,
                )
            )
            continue

        pending_para.append(stripped)

    flush_para()
    return story


def draw_footer(canvas, doc, title: str, styles: dict[str, ParagraphStyle]) -> None:
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#E2E8F0"))
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 13 * mm, A4[0] - doc.rightMargin, 13 * mm)
    footer = f"{title} | Page {doc.page}"
    canvas.setFont("STSong-Light", 7)
    canvas.setFillColor(colors.HexColor("#718096"))
    canvas.drawString(doc.leftMargin, 8 * mm, footer[:140])
    canvas.restoreState()


def convert_file(md_path: Path, font_name: str) -> Path:
    styles = make_styles(font_name)
    pdf_path = md_path.with_suffix(".pdf")
    markdown = md_path.read_text(encoding="utf-8", errors="replace")
    story = markdown_to_story(markdown, styles)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=15 * mm,
        bottomMargin=18 * mm,
        title=md_path.stem,
        author="Codex",
    )
    footer = lambda canvas, doc_obj: draw_footer(canvas, doc_obj, md_path.stem, styles)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return pdf_path


def main() -> None:
    font_name = register_fonts()
    md_files = sorted(REPORT_DIR.glob("*_business_report.md"))
    if not md_files:
        raise SystemExit(f"No Markdown business reports found in {REPORT_DIR}")

    for md_path in md_files:
        pdf_path = convert_file(md_path, font_name)
        print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
