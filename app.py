from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
import io
import os
from tables import sponsorship_table
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    email_text = ""
    subject = ""

    if request.method == "POST":
        company = request.form["company"]
        name_type = request.form["name_type"]
        name = request.form.get("name", "")
        who = request.form.get("who", "")
        title = request.form["title"]

        if name_type == "N":
            header = f"Hello {name},"
        elif name_type == "L":
            header = f"Dear {who}.{name},"
        else:
            header = f"Hello {company},"

        email_text = f"""{header}

I hope this message finds you well. I'm Illia Markov...
(keep your email text here)

Best regards,
Illia Markov
Teacher Mentor Contact: J. Levy, email J.Levy@TVDSB.ca
"""

        subject = title

    return render_template(
        "index.html",
        email=email_text,
        subject=subject
    )

#PDF
@app.route("/pdf", methods=["POST"])
def make_pdf():
    company = request.form["company"]
    name_type = request.form["name_type"]
    name = request.form.get("name", "")
    who = request.form.get("who", "")
    users_name = request.form.get("users_name", "")

    if name_type == "N":
        PDFheader1 = f"Hello {name},"
        PDFheader2 = f"Dear {name},"
    elif name_type == "L":
        PDFheader1 = f"Dear {who}.{name},"
        if who == "Mr":
            PDFheader2 = "Dear Sir,"
        else:
            PDFheader2 = "Dear Madam,"
    elif name_type == "C":
        PDFheader1 = f"Hello {name},"
        PDFheader2 = f"Dear {name},"

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(buffer, pagesize=LETTER)
    story = []
    styles['Normal'].fontSize = 12

    my_style = ParagraphStyle(
    name="MyStyle",
    parent = styles["Normal"],
    fontName="Times-Roman",
    fontSize=11.5,
    leading=14.5,       
    )   
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Westminster WildBOTS #6725</b>", styles['Normal']))

    story.append(Paragraph("Fall, 2025", my_style))
    story.append(Spacer(1, 24))

    story.append(Paragraph(PDFheader1, my_style))
    story.append(Spacer(1, 12))
    #============Page 1============#
    Body_Pagraph = "I am a member of the Westminster Secondary School robotics team, and we<br/>" \
    "are wondering if you would like to sponsor us!We are currently competing <br/>" \
    "in the FIRST Robotics competitions of 2026, and in order to move forward with our robot " \
    "building process, we are searching for supportive companies to help finance our team. "

    Body_Pagraph1 = "We currently need about $50,000 to fund our admission into the FIRST program ($9000), " \
    "purchase supplies to build the robot ($5000) and pay for our trips to the competitions (hotel and " \
    "transportation, $11000+ per 3 events). We are attending competitions at the Universities of " \
    "Waterloo and Windsor and hope to be invited again to Provincials. Being able to go to these" \
    "events allows our team to gain broader perspectives on technological applications and learn to " \
    "communicate and cooperate under stress. Our team is extremely excited for this year's " \
    "competition season, and we’re so ready for all the upcoming challenges and new experiences we " \
    "will face."

    Body_Pagraph2 ="We have 4 sponsorship packages: Silver, Gold, Platinum, and Diamond. Please see the attached " \
    "page for more information on these sponsorship opportunities."

    Body_Pagraph3 ="We thank you in advance for any help you can offer. If you are interested please contact our lead " \
    "mentor Mrs. Jennifer Levy at j.levy@tvdsb.ca."

    Body_Pagraphs4 = "Sincerely,<br/>" \
                     f"{users_name} <br/>" \
                     "WildBOTS #6725 <br/>" \
                     "230 Base Line Road West <br/>" \
                     "London, ON N6J 1W1 <br/>" \
                     "Tel: 519-452-2900 Fax: 519-452-2919 <br/>" \
                     "Email: <u><font color='#1155cc'>j.levy@tvdsb.ca</font></u><br/>" \
                     "Facebook: Westminster Wildbots Team 6725<br/>" \
                     "Instagram & Twitter: @Wildbots6725<br/>"
                    
    #============Page 3============#
    Body_PagraphP3 = "We’d like to introduce you to the most vibrant team at Westminster<br />" \
    "Secondary School: our robotics team. We are part of the international<br />" \
    "robotics competition FIRST Robotics (For Inspiration and Recognition of<br />" \
    "Science and Technology),which aims to encourage the passion of science and technology in the<br />" \
    "rising generations. Our students learn to build an enterprise which markets, designs, builds, and<br />" \
    "programs a robot which then competes with and against other high school teams’ robots. We also<br />" \
    "do outreach events in the school and community to encourage participation in STEM activities<br />" \
    "and education."

    Body_PagraphP3_1 ="Why is robotics called ‘the most difficult fun you’ll ever have’? The students don’t just learn <br />" \
    "real-world engineering: coding, electronics, design, etc., they also gain broader capabilities like <br />" \
    "problem solving, communication skills and tenacity. We have seen timid grade 9 students grow <br />" \
    "into bold, intuitive public speakers in just a few months through our program. Students who join <br />" \
    "us with just a keen interest in coding can learn to apply the math and physics they learn in their <br />" \
    "schoolwork to functional lines of code. When asked about the best part of their competition <br />" \
    "events, students always talk about the thrill of seeing all the problems they’ve solved along the <br />" \
    "way actually coming to fruition in their working robot. Our students work collaboratively late <br />" \
    "after school most days of the week: they are passionate."

    Body_PagraphP3_2 = "Many of our graduates continue in careers related to business or STEM and are confident, <br />" \
    "creative, capable leaders in their fields. When able, they return to the school to mentor the next <br />" \
    "young team because they see the tremendous value in the robotics experience. Investing in <br />" \
    "London robotics teams builds high-quality employees for Ontario’s future."

    Body_PagraphP3_3 = "We hope you will consider supporting us. <b>Please contact us for more information and check <br />" \
    "out our website for pictures and videos of the difficult -and amazing- things we do.</b>"

    #Easy way to change colours: <font color='#827241'>Gold </font>'

    Body_PagraphP3_4 = "Sincerely,<br />" \
                        "Jennifer Levy and Terry Williams<br />" \
                        "Lead Mentors<br />" \
                        "Team #6725 Westminster WildBOTS<br />" \
                        "email: <u><font color='#1155cc'>J.Levy@TVDSB.ca</font></u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u><font color='#1155cc'>T.Williams@TVDSB.ca</font></u><br />" \
                        "websites: Team #6725: <u><font color='#1155cc'>https://wildbots.wordpress.com/</font></u> FIRST:  <u><font color='#1155cc'>https://www.firstinspires.org/</font></u><br />"
                          

    story.append(Paragraph(Body_Pagraph, my_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph(Body_Pagraph1, my_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph(Body_Pagraph2, my_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph(Body_Pagraph3, my_style))
    story.append(Spacer(1, 16))

    story.append(Paragraph(Body_Pagraphs4, my_style))
    # jpg or png
    def background(canvas, doc):
        canvas.drawImage(
            "G:\Мій диск\P2 Coding\HTML\Images\PDF Sponsorship BACKGROUND+LINE.jpg",
            x=0,
            y=0,
            width=LETTER[0],
            height=LETTER[1]
        )
    
    

    # -------- PAGE 2 --------#
    story.append(PageBreak())
    #=======ADD THING HERE ========#
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Westminster WildBOTS #6725</b>", styles['Normal']))
    story.append(Paragraph("<b>Sponsorship Levels</b>", styles['Normal']))
    story.append(Spacer(1, 20))
    story.append(Paragraph("We appreciate all our sponsors at any level and would like to help you by <br/>" \
    "advertising for your company in various ways.", my_style))
    story.append(Spacer(1, 20))
    table = sponsorship_table(styles)
    table.hAlign = "LEFT"
    story.append(Spacer(1, 30))
    story.append(table)
    #=======ADD THING HERE ========#

    #-------- PAGE 3 --------#
    story.append(PageBreak())
    #=======ADD THING HERE ========#
    story.append(Spacer(1,8))
    story.append(Paragraph("Fall, 2025", my_style))
    story.append(Spacer(1,8))
    story.append(Spacer(1,8))
    story.append(Paragraph(PDFheader2, my_style))
    story.append(Spacer(1,8))
    story.append(Spacer(1,8))
    #story.append(Spacer(1,8)) easy copy and paste
    #story.append(Paragraph("",my_style)) easy copy and paste 
    story.append(Paragraph(Body_PagraphP3, my_style))
    story.append(Spacer(1,8))
    story.append(Paragraph(Body_PagraphP3_1, my_style))
    story.append(Spacer(1,8))
    story.append(Paragraph(Body_PagraphP3_2, my_style))
    story.append(Spacer(1,8))
    story.append(Paragraph(Body_PagraphP3_3, my_style))
    story.append(Spacer(1, 16))
    story.append(Paragraph(Body_PagraphP3_4, my_style))
    #=======ADD THING HERE ========#

    doc.build(
    story,
    onFirstPage=background,
    onLaterPages=background
    )
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"PDF Sponsorship, {company}.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)