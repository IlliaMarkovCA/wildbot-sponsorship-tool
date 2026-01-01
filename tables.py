from reportlab.platypus import (
    Paragraph, Table, TableStyle, ListFlowable, ListItem, Spacer
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def sponsorship_table(styles):
    body_style = ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=11.5,
        leading=14.5
    )

    def bullets(points):
        return ListFlowable(
            [ListItem(Paragraph(p, body_style)) for p in points],
            bulletType="bullet",
            leftIndent=22,
            bulletFontSize=12
        )

    silver = [
        Paragraph("With a Silver sponsorship, your company logo will be showcased on:", body_style),
        bullets([
            "Our team website and the pit wall",
            "On our robot (Small logo)"
        ])
    ]

    gold = [
        Paragraph("With a Gold sponsorship, your company logo will be showcased on:", body_style),
        bullets([
            "Our team website and the pit wall",
            "The back of our sweatshirts",
            "On our robot (Small logo)"
        ])
    ]

    platinum = [
        Paragraph("With a Platinum sponsorship, your company logo will be showcased on:", body_style),
        bullets([
            "Our team website and the pit wall",
            "The back of our sweatshirts",
            "On our robot (Medium logo)"
        ]),
        Spacer(1, 10),
        Paragraph(
            "You will also receive a shoutout on Instagram and a verbal mention at competitions.",
            body_style
        )
    ]

    diamond = [
        Paragraph("With a Diamond sponsorship, your company logo will be showcased on:", body_style),
        bullets([
            "Our website and the pit wall",
            "The back of our sweatshirts (Large logo)",
            "Our robot (Large logo)"
        ]),
        Spacer(1, 10),
        Paragraph(
            "You will also receive a shoutout on Instagram and a verbal mention at competitions.",
            body_style
        )
    ]

    table_data = [
        [Paragraph("Silver <b>$100+</b>", body_style), silver],
        [Paragraph("Gold <b>$500+</b>", body_style), gold],
        [Paragraph("Platinum <b>$1000+</b>", body_style), platinum],
        [Paragraph("Diamond <b>$2000+</b>", body_style), diamond],
    ]

    table = Table(table_data, colWidths=[109, 354]) #Just enouph to fit the text 90, 335 

    WILDBOTS_GOLD = colors.HexColor("#eaddb5")
    WILDBOTS_LIGHT_GOLD = colors.HexColor("#f3eddb")
    WILDBOTS_DARK_GOLD = colors.HexColor("#827241")

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), WILDBOTS_GOLD),
        ("BACKGROUND", (1, 0), (-1, -1), WILDBOTS_LIGHT_GOLD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 1.5, WILDBOTS_DARK_GOLD),
    ]))

    return table