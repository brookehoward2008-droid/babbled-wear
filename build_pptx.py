"""Build the Save-Images-as-PDF training deck as a real .pptx file."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

PINK = RGBColor(0xFF, 0x2D, 0x87)
PURPLE = RGBColor(0x7B, 0x2C, 0xBF)
YELLOW = RGBColor(0xFF, 0xD6, 0x0A)
INK = RGBColor(0x0F, 0x0F, 0x14)
PAPER = RGBColor(0xFA, 0xFA, 0xFA)
DIM = RGBColor(0xCC, 0xCC, 0xD0)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_bg(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    fill(bg, INK)
    # accent bars
    top = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, Inches(0.18))
    fill(top, PINK)
    bot = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, SH - Inches(0.10), SW, Inches(0.10))
    fill(bot, YELLOW)


def add_text(slide, left, top, width, height, text, *, size=24, bold=False,
             color=PAPER, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    if isinstance(text, str):
        text = [text]
    for i, line in enumerate(text):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = "Calibri"
    return tb


def eyebrow(slide, text):
    add_text(slide, Inches(0.7), Inches(0.45), Inches(12), Inches(0.45),
             text.upper(), size=14, bold=True, color=YELLOW)


def title(slide, text, *, size=48, color=PAPER):
    add_text(slide, Inches(0.7), Inches(0.95), Inches(12), Inches(1.6),
             text, size=size, bold=True, color=color)


def body(slide, lines, *, top=2.8, size=22, color=PAPER, bold=False, height=4.0):
    add_text(slide, Inches(0.7), Inches(top), Inches(12), Inches(height),
             lines, size=size, color=color, bold=bold)


def bullets(slide, items, *, top=2.6, size=22, height=4.4):
    tb = slide.shapes.add_textbox(Inches(0.7), Inches(top), Inches(12), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(8)
        run = p.add_run()
        run.text = "• " + item
        run.font.size = Pt(size)
        run.font.color.rgb = PAPER
        run.font.name = "Calibri"


def steps(slide, items, *, top=2.4, size=22, width=12):
    tb = slide.shapes.add_textbox(Inches(0.7), Inches(top), Inches(width), Inches(4.6))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(10)
        num = p.add_run()
        num.text = f" {i+1}.  "
        num.font.size = Pt(size + 2)
        num.font.bold = True
        num.font.color.rgb = PINK
        num.font.name = "Calibri"
        rest = p.add_run()
        rest.text = item
        rest.font.size = Pt(size)
        rest.font.color.rgb = PAPER
        rest.font.name = "Calibri"


# ---------- Slide 1: Title ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Training Presentation")
add_text(s, Inches(0.7), Inches(1.4), Inches(8.5), Inches(2.4),
         "Save Images as a PDF", size=58, bold=True, color=PINK)
add_text(s, Inches(0.7), Inches(2.7), Inches(8.5), Inches(1.0),
         "— Using Print.", size=42, bold=True, color=YELLOW)
add_text(s, Inches(0.7), Inches(4.3), Inches(8.5), Inches(1.6),
         "A simple skill that works on almost any device, with no extra software to install.",
         size=22, color=PAPER)
add_text(s, Inches(0.7), Inches(6.3), Inches(8.5), Inches(0.6),
         "By Brooke Chauntel  ·  BaBBled.", size=16, color=DIM)
s.shapes.add_picture("img/training/pdf-icon.png",
                     Inches(9.5), Inches(1.4), height=Inches(5.0))

# ---------- Slide 2: Hook ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Why this matters")
title(s, "Ever needed to email a photo as a PDF?", size=40, color=PAPER)
bullets(s, [
    "Job applications and résumé portfolios often require PDF.",
    "Schools and instructors often only accept PDF submissions.",
    "PDFs keep multiple images together in one tidy file.",
    "PDFs print and view the same on every device.",
])
add_text(s, Inches(0.7), Inches(6.3), Inches(12), Inches(0.6),
         "No Adobe. No paid app. Just the Print dialog you already have.",
         size=18, bold=True, color=YELLOW)

# ---------- Slide 3: Objectives ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Today you will learn")
title(s, "By the end of this training, you'll be able to…", size=36)
bullets(s, [
    "Open one or more images on your computer or phone.",
    "Use the Print command to reach a hidden PDF option.",
    "Choose \"Save as PDF\" as the destination.",
    "Adjust orientation, size, and margins for a clean result.",
    "Save the finished PDF where you can find it later.",
])

# ---------- Slide 4: What you need ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Before we start")
title(s, "What you need", size=44)
cards = [
    ("A device", "Windows PC, Mac, Chromebook, iPhone, or Android — all work."),
    ("Your image(s)", "JPG, PNG, HEIC, or screenshots already saved on the device."),
    ("A folder in mind", "Decide where you want the finished PDF to land (Desktop, Downloads, etc.)."),
    ("A file name", "Something clear like 'brooke-portfolio.pdf', not 'untitled1.pdf'."),
]
positions = [(0.7, 2.6), (6.95, 2.6), (0.7, 4.95), (6.95, 4.95)]
for (heading, copy), (l, t) in zip(cards, positions):
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t),
                              Inches(5.95), Inches(2.05))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(0x1C, 0x1C, 0x26)
    card.line.color.rgb = PURPLE
    card.line.width = Pt(1.5)
    add_text(s, Inches(l + 0.25), Inches(t + 0.18), Inches(5.5), Inches(0.5),
             heading, size=22, bold=True, color=YELLOW)
    add_text(s, Inches(l + 0.25), Inches(t + 0.85), Inches(5.5), Inches(1.1),
             copy, size=17, color=PAPER)

# ---------- Slide 5: Windows ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Method 1 · Windows")
title(s, "Save an image as PDF on Windows", size=34)
steps(s, [
    "Open the image — double-click it so it opens in Photos.",
    "Press Ctrl + P to open the Print dialog.",
    "Under Printer, choose \"Microsoft Print to PDF.\"",
    "Pick paper size and orientation, then click Print.",
    "Name the file and choose where to save it. Done.",
], size=18, width=6.5)
s.shapes.add_picture("img/training/windows-print-dialog.png",
                     Inches(7.2), Inches(2.0), width=Inches(5.7))

# ---------- Slide 6: Mac ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Method 2 · Mac")
title(s, "Save an image as PDF on a Mac", size=34)
steps(s, [
    "Open the image in Preview (double-click it).",
    "Press ⌘ + P to open Print.",
    "In the bottom-left, click the PDF dropdown.",
    "Choose \"Save as PDF.\"",
    "Name it, pick a folder, click Save.",
], size=18, width=6.5)
s.shapes.add_picture("img/training/mac-print-dialog.png",
                     Inches(7.2), Inches(2.0), width=Inches(5.7))
add_text(s, Inches(0.7), Inches(6.7), Inches(12.5), Inches(0.5),
         "Bonus: in Finder, select images → right-click → Quick Actions → Create PDF.",
         size=14, bold=True, color=YELLOW)

# ---------- Slide 7: Phone ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Method 3 · Phone")
title(s, "Save an image as PDF on your phone", size=32)
steps(s, [
    "Open the image in your Photos or Gallery app.",
    "Tap the Share button (the box with the arrow).",
    "Scroll down and tap Print.",
    "Pinch out with two fingers on the preview (iPhone) or tap the PDF icon (Android).",
    "Tap Share / Save → Save to Files.",
], size=18, width=8.0)
s.shapes.add_picture("img/training/iphone-share-sheet.png",
                     Inches(9.0), Inches(1.6), height=Inches(5.6))

# ---------- Slide 8: Multiple ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Pro move")
title(s, "Putting multiple images in one PDF", size=36)
s.shapes.add_picture("img/training/multi-to-one.png",
                     Inches(2.5), Inches(1.9), width=Inches(8.5))
bullets(s, [
    "Windows: File Explorer → select images → right-click → Print → \"Microsoft Print to PDF.\"",
    "Mac: Finder → select images → right-click → Quick Actions → Create PDF.",
    "Phone: Photos → Select → Share → Print → pinch out.",
], top=5.5, size=18)
add_text(s, Inches(0.7), Inches(6.85), Inches(12), Inches(0.5),
         "One PDF beats five attachments — every time.",
         size=15, bold=True, color=YELLOW)

# ---------- Slide 9: Shortcut — Export → PDF ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Shortcut")
title(s, "Skip the Print dialog with Export → PDF", size=34)
add_text(s, Inches(0.7), Inches(2.0), Inches(12), Inches(0.7),
         "Some apps offer a one-step PDF export. Always check the File menu first.",
         size=20, color=PAPER)
shortcut_cards = [
    ("Word · PowerPoint",
     "File  →  Export  →  Create PDF/XPS Document"),
    ("Pages · Numbers · Keynote",
     "File  →  Export To  →  PDF…"),
    ("Photos (Mac)",
     "File  →  Export  →  Save PDF to…"),
    ("Google Docs · Slides · Sheets",
     "File  →  Download  →  PDF Document (.pdf)"),
]
positions = [(0.7, 2.9), (6.95, 2.9), (0.7, 5.0), (6.95, 5.0)]
for (heading, copy), (l, t) in zip(shortcut_cards, positions):
    cardshape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t),
                                   Inches(5.95), Inches(1.85))
    cardshape.fill.solid()
    cardshape.fill.fore_color.rgb = RGBColor(0x1C, 0x1C, 0x26)
    cardshape.line.color.rgb = YELLOW
    cardshape.line.width = Pt(1.5)
    add_text(s, Inches(l + 0.25), Inches(t + 0.18), Inches(5.5), Inches(0.5),
             heading, size=20, bold=True, color=YELLOW)
    add_text(s, Inches(l + 0.25), Inches(t + 0.78), Inches(5.5), Inches(1.0),
             copy, size=18, color=PAPER)
add_text(s, Inches(0.7), Inches(7.05), Inches(12), Inches(0.5),
         "If \"Export\" isn't there, fall back to the Print method we just learned.",
         size=14, bold=True, color=YELLOW)

# ---------- Slide 10: Now you try (interactive sandbox) ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Now you try · Interactive sandbox")
title(s, "Practice on a real page, live in your browser.", size=32)
add_text(s, Inches(0.7), Inches(2.0), Inches(8.3), Inches(0.7),
         "Scan the QR code or open the link below. Drop in any photos, then tap \"Save as PDF.\"",
         size=18, color=PAPER)

# Three activity tiers as cards (left side)
tiers = [
    ("EASY",  "Drop in 1 photo. Save it as 'first.pdf'."),
    ("MEDIUM", "Drop in 3 photos. Save them as one combined PDF."),
    ("BONUS", "Change the title field, then save. Open the PDF — does the title match?"),
]
for i, (tag, copy) in enumerate(tiers):
    ty = 3.05 + i * 0.95
    cardshape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                   Inches(0.7), Inches(ty), Inches(8.3), Inches(0.85))
    cardshape.fill.solid()
    cardshape.fill.fore_color.rgb = RGBColor(0x1C, 0x1C, 0x26)
    cardshape.line.color.rgb = PINK
    cardshape.line.width = Pt(1.5)
    add_text(s, Inches(0.95), Inches(ty + 0.18), Inches(1.6), Inches(0.55),
             tag, size=18, bold=True, color=YELLOW)
    add_text(s, Inches(2.5), Inches(ty + 0.18), Inches(6.4), Inches(0.55),
             copy, size=17, color=PAPER)

# QR code on the right
s.shapes.add_picture("img/training/sandbox-qr.png",
                     Inches(9.4), Inches(2.0), width=Inches(3.4))
add_text(s, Inches(9.2), Inches(5.5), Inches(3.9), Inches(0.5),
         "Scan to open", size=14, bold=True, color=YELLOW, align=PP_ALIGN.CENTER)
add_text(s, Inches(9.2), Inches(5.85), Inches(3.9), Inches(0.5),
         "babbled-wear/sandbox", size=15, bold=True, color=PAPER, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.7), Inches(6.7), Inches(12), Inches(0.5),
         "Stuck? Raise your hand — I'll come help.",
         size=16, color=PAPER)

# ---------- Slide 11: Pitfalls ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Watch out for")
title(s, "Three things that trip people up", size=38)
pitfalls = [
    ("1. Wrong destination",
     "If your real printer is selected, it'll print on paper. Always switch the destination to Save as PDF."),
    ("2. Cropped image",
     "If the photo is cut off, change orientation to Landscape or shrink margins to None."),
    ("3. Lost file",
     "Note the folder before you click Save. Default is usually Documents or Downloads."),
    ("Bonus: huge file size",
     "If the PDF is too big to email, lower print quality to Standard or use a smaller paper size."),
]
positions = [(0.7, 2.6), (6.95, 2.6), (0.7, 4.95), (6.95, 4.95)]
for (heading, copy), (l, t) in zip(pitfalls, positions):
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t),
                              Inches(5.95), Inches(2.05))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(0x1C, 0x1C, 0x26)
    card.line.color.rgb = PINK
    card.line.width = Pt(1.5)
    add_text(s, Inches(l + 0.25), Inches(t + 0.18), Inches(5.5), Inches(0.5),
             heading, size=20, bold=True, color=PINK)
    add_text(s, Inches(l + 0.25), Inches(t + 0.85), Inches(5.5), Inches(1.1),
             copy, size=16, color=PAPER)

# ---------- Slide 12: Recap ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Quick recap")
title(s, "The whole skill in five words:", size=40)
add_text(s, Inches(0.7), Inches(2.6), Inches(12), Inches(1.4),
         "Open. Print. Save as PDF.", size=56, bold=True, color=PINK)
bullets(s, [
    "Works on Windows, Mac, Chromebook, iPhone, and Android.",
    "No software to download, no account to make.",
    "Combine multiple images by selecting them all first.",
    "Name your file something you can find later.",
], top=4.4, size=20, height=3.0)

# ---------- Slide 13: Final tips + thanks ----------
s = prs.slides.add_slide(BLANK)
add_bg(s)
eyebrow(s, "Final tips")
title(s, "Two habits that will save you time", size=40)
bullets(s, [
    "Make a folder called PDFs so you stop hunting for them.",
    "Double-click the saved PDF to verify it looks right before you send it.",
])
add_text(s, Inches(0.7), Inches(5.3), Inches(12), Inches(0.9),
         "Thank you for your attention — and for practicing along.",
         size=28, bold=True, color=YELLOW)
add_text(s, Inches(0.7), Inches(6.3), Inches(12), Inches(0.6),
         "Questions? Ask away.", size=20, color=PAPER)

OUT = "Save-Images-as-PDF-Using-Print.pptx"
prs.save(OUT)
print(f"Saved: {OUT}")
