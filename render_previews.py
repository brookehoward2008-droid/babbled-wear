"""Render each slide to a PNG so they can be previewed inline."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1600, 900
OUT = "slide_previews"
os.makedirs(OUT, exist_ok=True)

PINK = (0xFF, 0x2D, 0x87)
PURPLE = (0x7B, 0x2C, 0xBF)
YELLOW = (0xFF, 0xD6, 0x0A)
INK = (0x0F, 0x0F, 0x14)
PAPER = (0xFA, 0xFA, 0xFA)
DIM = (0xCC, 0xCC, 0xD0)
CARD = (0x1C, 0x1C, 0x26)

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
BOLD_PATH = FONT_PATHS[0]
REG_PATH = FONT_PATHS[1]

def font(size, bold=False):
    return ImageFont.truetype(BOLD_PATH if bold else REG_PATH, size)

def wrap(draw, text, fnt, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, fnt, color, max_w, line_gap=8):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        bbox = draw.textbbox((0, 0), line, font=fnt)
        y += (bbox[3] - bbox[1]) + line_gap
    return y

def base():
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    # gradient hint via two soft rectangles
    overlay = Image.new("RGB", (W, H), INK)
    od = ImageDraw.Draw(overlay)
    # subtle accent blocks
    od.ellipse((-200, -200, 700, 700), fill=(50, 20, 60))
    od.ellipse((1000, 400, 1900, 1300), fill=(80, 30, 95))
    img = Image.blend(img, overlay, 0.55)
    d = ImageDraw.Draw(img)
    # top + bottom bars
    d.rectangle((0, 0, W, 14), fill=PINK)
    d.rectangle((0, H - 8, W, H), fill=YELLOW)
    return img, d

def eyebrow(d, text):
    d.text((90, 60), text.upper(), font=font(20, True), fill=YELLOW)

def title(d, text, size=70, color=PAPER, y=120):
    f = font(size, True)
    return draw_wrapped(d, 90, y, text, f, color, W - 180, line_gap=6)

def bullets(d, items, y=350, size=30):
    f = font(size)
    for it in items:
        d.text((110, y), "•", font=font(size, True), fill=PINK)
        bottom = draw_wrapped(d, 150, y, it, f, PAPER, W - 260, line_gap=4)
        y = bottom + 12
    return y

def steps_render(d, items, y=300, size=30):
    f = font(size)
    fb = font(size + 2, True)
    for i, it in enumerate(items, 1):
        d.text((100, y), f"{i}.", font=fb, fill=PINK)
        bottom = draw_wrapped(d, 170, y, it, f, PAPER, W - 280, line_gap=4)
        y = bottom + 14
    return y

def card(d, x, y, w, h, heading, copy, border=PURPLE, hcolor=YELLOW):
    d.rounded_rectangle((x, y, x + w, y + h), radius=18, fill=CARD, outline=border, width=2)
    d.text((x + 30, y + 22), heading, font=font(26, True), fill=hcolor)
    draw_wrapped(d, x + 30, y + 70, copy, font(20), PAPER, w - 60, line_gap=4)

slides = []

# 1 Title
img, d = base()
eyebrow(d, "Training Presentation")
title(d, "Save Images as a PDF", size=92, color=PINK, y=150)
title(d, "— Using Print.", size=64, color=YELLOW, y=300)
draw_wrapped(d, 90, 460, "A simple skill that works on almost any device, with no extra software to install.",
             font(30), PAPER, W - 180, line_gap=6)
d.text((90, H - 70), "By Brooke Chauntel  ·  BaBBled.", font=font(18), fill=DIM)
slides.append(img)

# 2 Hook
img, d = base()
eyebrow(d, "Why this matters")
title(d, "Ever needed to email a photo as a PDF?", size=58)
bullets(d, [
    "Job applications and résumé portfolios often require PDF.",
    "Schools and instructors often only accept PDF submissions.",
    "PDFs keep multiple images together in one tidy file.",
    "PDFs print and view the same on every device.",
], y=320, size=28)
d.text((90, H - 80), "No Adobe. No paid app. Just the Print dialog you already have.",
       font=font(22, True), fill=YELLOW)
slides.append(img)

# 3 Objectives
img, d = base()
eyebrow(d, "Today you will learn")
title(d, "By the end of this training, you'll be able to…", size=48)
bullets(d, [
    "Open one or more images on your computer or phone.",
    "Use the Print command to reach a hidden PDF option.",
    "Choose \"Save as PDF\" as the destination.",
    "Adjust orientation, size, and margins for a clean result.",
    "Save the finished PDF where you can find it later.",
], y=290, size=28)
slides.append(img)

# 4 What you need
img, d = base()
eyebrow(d, "Before we start")
title(d, "What you need", size=72)
cards = [
    ("A device", "Windows PC, Mac, Chromebook, iPhone, or Android — all work."),
    ("Your image(s)", "JPG, PNG, HEIC, or screenshots already saved on the device."),
    ("A folder in mind", "Decide where you want the finished PDF to land (Desktop, Downloads, etc.)."),
    ("A file name", "Something clear like 'brooke-portfolio.pdf', not 'untitled1.pdf'."),
]
positions = [(90, 320), (820, 320), (90, 590), (820, 590)]
for (h_, c_), (x, y) in zip(cards, positions):
    card(d, x, y, 690, 240, h_, c_)
slides.append(img)

# 5 Windows
img, d = base()
eyebrow(d, "Method 1 · Windows")
title(d, "Save an image as PDF on Windows", size=54)
steps_render(d, [
    "Open the image — double-click it so it opens in Photos.",
    "Press Ctrl + P to open the Print dialog.",
    "Under Printer, choose \"Microsoft Print to PDF.\"",
    "Pick paper size and orientation, then click Print.",
    "Name the file and choose where to save it. Done.",
], y=290, size=28)
slides.append(img)

# 6 Mac
img, d = base()
eyebrow(d, "Method 2 · Mac")
title(d, "Save an image as PDF on a Mac", size=54)
steps_render(d, [
    "Open the image in Preview (double-click it).",
    "Press Command + P to open Print.",
    "In the bottom-left, click the PDF dropdown.",
    "Choose \"Save as PDF.\"",
    "Name it, pick a folder, click Save.",
], y=290, size=28)
d.text((90, H - 80), "Bonus: in Finder, select images → right-click → Quick Actions → Create PDF.",
       font=font(20, True), fill=YELLOW)
slides.append(img)

# 7 Phone
img, d = base()
eyebrow(d, "Method 3 · Phone")
title(d, "Save an image as PDF on your phone", size=54)
steps_render(d, [
    "Open the image in your Photos or Gallery app.",
    "Tap the Share button (the box with the arrow).",
    "Scroll down and tap Print.",
    "Pinch out with two fingers (iPhone) or tap the PDF icon (Android).",
    "Tap Share / Save → Save to Files.",
], y=290, size=28)
slides.append(img)

# 8 Multiple
img, d = base()
eyebrow(d, "Pro move")
title(d, "Putting multiple images in one PDF", size=54)
bullets(d, [
    "Windows: select all images in File Explorer → right-click → Print → \"Microsoft Print to PDF.\"",
    "Mac: select images in Finder → right-click → Quick Actions → Create PDF.",
    "Phone: in Photos, tap Select, choose images, then Share → Print → pinch out.",
], y=320, size=26)
d.text((90, H - 80), "One PDF beats five attachments — every time.",
       font=font(22, True), fill=YELLOW)
slides.append(img)

# 9 Activity
img, d = base()
eyebrow(d, "Your turn")
title(d, "Try it with me — 60 seconds.", size=64)
bullets(d, [
    "Pick any photo on your device.",
    "Open it. Hit Print.",
    "Choose \"Save as PDF.\"",
    "Save it to your Desktop as test.pdf.",
], y=350, size=30)
d.text((90, H - 90), "Raise your hand if you get stuck — I'll come help.",
       font=font(22), fill=PAPER)
slides.append(img)

# 10 Pitfalls
img, d = base()
eyebrow(d, "Watch out for")
title(d, "Three things that trip people up", size=54)
pitfalls = [
    ("1. Wrong destination", "If your real printer is selected, it'll print on paper. Switch destination to Save as PDF."),
    ("2. Cropped image", "If the photo is cut off, change orientation to Landscape or shrink margins to None."),
    ("3. Lost file", "Note the folder before you click Save. Default is usually Documents or Downloads."),
    ("Bonus: huge file size", "If the PDF is too big to email, lower print quality or use a smaller paper size."),
]
positions = [(90, 320), (820, 320), (90, 590), (820, 590)]
for (h_, c_), (x, y) in zip(pitfalls, positions):
    card(d, x, y, 690, 240, h_, c_, border=PINK, hcolor=PINK)
slides.append(img)

# 11 Recap
img, d = base()
eyebrow(d, "Quick recap")
title(d, "The whole skill in five words:", size=56)
title(d, "Open. Print. Save as PDF.", size=72, color=PINK, y=320)
bullets(d, [
    "Works on Windows, Mac, Chromebook, iPhone, and Android.",
    "No software to download, no account to make.",
    "Combine multiple images by selecting them all first.",
    "Name your file something you can find later.",
], y=520, size=24)
slides.append(img)

# 12 Thanks
img, d = base()
eyebrow(d, "Final tips")
title(d, "Two habits that will save you time", size=54)
bullets(d, [
    "Make a folder called PDFs so you stop hunting for them.",
    "Double-click the saved PDF to verify it looks right before you send it.",
], y=320, size=28)
d.text((90, 580), "Thank you for your attention — and for practicing along.",
       font=font(36, True), fill=YELLOW)
d.text((90, 660), "Questions? Ask away.", font=font(26), fill=PAPER)
slides.append(img)

# save individuals + combined contact sheet
for i, s in enumerate(slides, 1):
    s.save(f"{OUT}/slide-{i:02d}.png")

cols, rows = 2, 6
tw, th = W // 3, H // 3
sheet = Image.new("RGB", (tw * cols + (cols+1)*20, th * rows + (rows+1)*20), (10, 10, 14))
for i, s in enumerate(slides):
    thumb = s.resize((tw, th), Image.LANCZOS)
    r, c = divmod(i, cols)
    x = 20 + c * (tw + 20)
    y = 20 + r * (th + 20)
    sheet.paste(thumb, (x, y))
sheet.save(f"{OUT}/all-slides.png")
print(f"Wrote {len(slides)} slide PNGs and contact sheet to {OUT}/")
