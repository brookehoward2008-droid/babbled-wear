"""Generate mock UI illustrations of the Print dialog on each platform.

These aren't pixel-perfect screenshots — they're clean, readable diagrams
that show the user where to look for "Save as PDF" without exposing real
desktop content.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "img/training"
os.makedirs(OUT, exist_ok=True)

PINK = (0xFF, 0x2D, 0x87)
PURPLE = (0x7B, 0x2C, 0xBF)
YELLOW = (0xFF, 0xD6, 0x0A)
PAPER = (0xFA, 0xFA, 0xFA)
INK = (0x0F, 0x0F, 0x14)

LIGHT_BG = (0xF3, 0xF4, 0xF8)
WIN_BG = (0xFF, 0xFF, 0xFF)
WIN_HEADER = (0xF0, 0xF0, 0xF0)
WIN_ACCENT = (0x00, 0x78, 0xD4)
TEXT = (0x1A, 0x1A, 0x1F)
TEXT_DIM = (0x6B, 0x6B, 0x70)
BORDER = (0xC8, 0xC8, 0xCE)
HIGHLIGHT = (0xFF, 0xF4, 0xC4)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(s, b=False):
    return ImageFont.truetype(BOLD if b else REG, s)


def arrow(d, x, y, color=PINK, size=40):
    """Big pink arrow pointing right at (x, y)."""
    d.polygon([
        (x, y), (x + size, y - size // 2), (x + size, y - 8),
        (x + size + 30, y - 8), (x + size + 30, y + 8),
        (x + size, y + 8), (x + size, y + size // 2),
    ], fill=color)


# ---------- 1. Windows Print Dialog ----------
def windows_dialog():
    W, H = 1100, 750
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)

    # Window
    win_x, win_y, win_w, win_h = 60, 60, 980, 630
    d.rounded_rectangle((win_x, win_y, win_x + win_w, win_y + win_h),
                        radius=10, fill=WIN_BG, outline=BORDER, width=2)
    # Title bar
    d.rounded_rectangle((win_x, win_y, win_x + win_w, win_y + 50),
                        radius=10, fill=WIN_HEADER)
    d.rectangle((win_x, win_y + 25, win_x + win_w, win_y + 50), fill=WIN_HEADER)
    d.text((win_x + 24, win_y + 14), "Print", font=f(20, True), fill=TEXT)
    # Close X
    d.text((win_x + win_w - 38, win_y + 12), "×", font=f(28, True), fill=TEXT)

    # Body
    bx, by = win_x + 40, win_y + 90
    d.text((bx, by), "Printer", font=f(16), fill=TEXT_DIM)

    # Printer dropdown — highlighted
    drop_y = by + 30
    d.rounded_rectangle((bx, drop_y, bx + 580, drop_y + 56),
                        radius=6, fill=HIGHLIGHT, outline=PINK, width=3)
    d.text((bx + 18, drop_y + 14), "Microsoft Print to PDF", font=f(22, True), fill=TEXT)
    # caret
    d.polygon([(bx + 540, drop_y + 24), (bx + 560, drop_y + 24),
               (bx + 550, drop_y + 38)], fill=TEXT)

    # Arrow + label
    arrow(d, bx + 610, drop_y + 28, color=PINK, size=36)
    d.text((bx + 690, drop_y + 4), "Choose this", font=f(22, True), fill=PINK)
    d.text((bx + 690, drop_y + 32), "as your printer", font=f(20), fill=TEXT)

    # Other field rows (greyed)
    rows = [("Copies", "1"), ("Layout", "Portrait"), ("Paper size", "Letter (8.5 × 11 in)"),
            ("Color", "Color"), ("Pages", "All pages")]
    ry = drop_y + 100
    for label, value in rows:
        d.text((bx, ry), label, font=f(14), fill=TEXT_DIM)
        d.rounded_rectangle((bx, ry + 22, bx + 580, ry + 60),
                            radius=6, fill=WIN_BG, outline=BORDER, width=1)
        d.text((bx + 18, ry + 32), value, font=f(16), fill=TEXT)
        ry += 78

    # Print button
    btn_x = win_x + win_w - 240
    btn_y = win_y + win_h - 80
    d.rounded_rectangle((btn_x, btn_y, btn_x + 180, btn_y + 50),
                        radius=8, fill=WIN_ACCENT)
    d.text((btn_x + 60, btn_y + 14), "Print", font=f(20, True), fill=PAPER)
    d.rounded_rectangle((btn_x - 130, btn_y, btn_x - 10, btn_y + 50),
                        radius=8, fill=WIN_BG, outline=BORDER, width=2)
    d.text((btn_x - 90, btn_y + 14), "Cancel", font=f(18), fill=TEXT)

    img.save(f"{OUT}/windows-print-dialog.png")


# ---------- 2. Mac Print Dialog ----------
def mac_dialog():
    W, H = 1100, 750
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)

    win_x, win_y, win_w, win_h = 60, 60, 980, 630
    d.rounded_rectangle((win_x, win_y, win_x + win_w, win_y + win_h),
                        radius=14, fill=WIN_BG, outline=BORDER, width=2)
    # Title bar
    d.rounded_rectangle((win_x, win_y, win_x + win_w, win_y + 44),
                        radius=14, fill=(0xEC, 0xEC, 0xEE))
    d.rectangle((win_x, win_y + 22, win_x + win_w, win_y + 44), fill=(0xEC, 0xEC, 0xEE))
    # traffic lights
    for i, col in enumerate([(0xFF, 0x60, 0x5C), (0xFF, 0xBD, 0x44), (0x27, 0xC9, 0x3F)]):
        cx = win_x + 18 + i * 22
        d.ellipse((cx, win_y + 14, cx + 14, win_y + 28), fill=col)
    d.text((win_x + win_w // 2 - 30, win_y + 12), "Print", font=f(18, True), fill=TEXT)

    # Preview area (left)
    prev_x = win_x + 30
    prev_y = win_y + 70
    d.rounded_rectangle((prev_x, prev_y, prev_x + 380, prev_y + 480),
                        radius=4, fill=WIN_BG, outline=BORDER, width=2)
    # mock photo content
    d.rectangle((prev_x + 20, prev_y + 20, prev_x + 360, prev_y + 280),
                fill=(0x40, 0x20, 0x55))
    d.ellipse((prev_x + 80, prev_y + 60, prev_x + 300, prev_y + 240), fill=PINK)
    d.text((prev_x + 130, prev_y + 320), "your-photo.jpg", font=f(16), fill=TEXT_DIM)

    # Right column - settings
    rx = win_x + 440
    ry = win_y + 80
    rows = [("Printer:", "Brother HL-L2300D"),
            ("Presets:", "Default Settings"),
            ("Copies:", "1"),
            ("Pages:", "All"),
            ("Paper Size:", "US Letter")]
    for label, value in rows:
        d.text((rx, ry), label, font=f(15, True), fill=TEXT)
        d.rounded_rectangle((rx + 130, ry - 6, rx + 460, ry + 26),
                            radius=4, fill=WIN_BG, outline=BORDER, width=1)
        d.text((rx + 144, ry), value, font=f(14), fill=TEXT)
        ry += 44

    # Bottom: PDF dropdown — highlighted
    pdf_x = win_x + 30
    pdf_y = win_y + win_h - 70
    d.rounded_rectangle((pdf_x, pdf_y, pdf_x + 200, pdf_y + 44),
                        radius=8, fill=HIGHLIGHT, outline=PINK, width=3)
    d.text((pdf_x + 22, pdf_y + 10), "PDF", font=f(20, True), fill=TEXT)
    d.polygon([(pdf_x + 160, pdf_y + 16), (pdf_x + 180, pdf_y + 16),
               (pdf_x + 170, pdf_y + 30)], fill=TEXT)

    # Arrow + callout
    arrow(d, pdf_x + 220, pdf_y + 22, color=PINK, size=32)
    d.text((pdf_x + 295, pdf_y - 6), "Click here", font=f(20, True), fill=PINK)
    d.text((pdf_x + 295, pdf_y + 22), "→ Save as PDF", font=f(18), fill=TEXT)

    # Print button
    btn_x = win_x + win_w - 220
    btn_y = win_y + win_h - 70
    d.rounded_rectangle((btn_x, btn_y, btn_x + 180, btn_y + 44),
                        radius=10, fill=WIN_ACCENT)
    d.text((btn_x + 70, btn_y + 12), "Print", font=f(18, True), fill=PAPER)

    img.save(f"{OUT}/mac-print-dialog.png")


# ---------- 3. iPhone Share Sheet ----------
def iphone_share():
    W, H = 800, 1100
    img = Image.new("RGB", (W, H), (0x1C, 0x1C, 0x1E))
    d = ImageDraw.Draw(img)

    # phone frame
    fx, fy, fw, fh = 80, 80, W - 160, H - 160
    d.rounded_rectangle((fx, fy, fx + fw, fy + fh), radius=50,
                        fill=(0x00, 0x00, 0x00), outline=(0x33, 0x33, 0x36), width=4)
    # screen inset
    sx, sy, sw, sh = fx + 18, fy + 18, fw - 36, fh - 36
    d.rounded_rectangle((sx, sy, sx + sw, sy + sh), radius=38,
                        fill=(0xF2, 0xF2, 0xF7))
    # notch
    d.rounded_rectangle((sx + sw // 2 - 70, sy, sx + sw // 2 + 70, sy + 24),
                        radius=12, fill=(0x00, 0x00, 0x00))

    # status bar
    d.text((sx + 30, sy + 30), "9:41", font=f(18, True), fill=TEXT)
    d.text((sx + sw - 80, sy + 30), "100%", font=f(16, True), fill=TEXT)

    # Share sheet title
    d.text((sx + 30, sy + 90), "Share", font=f(28, True), fill=TEXT)
    # photo preview pill
    d.rounded_rectangle((sx + 30, sy + 140, sx + sw - 30, sy + 220),
                        radius=14, fill=WIN_BG, outline=BORDER, width=1)
    d.rounded_rectangle((sx + 50, sy + 160, sx + 110, sy + 200),
                        radius=8, fill=PINK)
    d.text((sx + 130, sy + 158), "1 Photo", font=f(18, True), fill=TEXT)
    d.text((sx + 130, sy + 184), "Today, 9:41 AM", font=f(14), fill=TEXT_DIM)

    # action rows
    actions = [
        ("AirDrop", False),
        ("Messages", False),
        ("Mail", False),
        ("Save to Files", False),
        ("Print", True),
        ("Add to Notes", False),
    ]
    ay = sy + 260
    for label, highlighted in actions:
        if highlighted:
            d.rounded_rectangle((sx + 24, ay - 6, sx + sw - 24, ay + 56),
                                radius=10, fill=HIGHLIGHT, outline=PINK, width=3)
        # icon box
        d.rounded_rectangle((sx + 40, ay, sx + 40 + 50, ay + 50),
                            radius=10, fill=(0xE8, 0xE8, 0xED))
        # printer-ish glyph for highlighted row
        if highlighted:
            d.rectangle((sx + 50, ay + 14, sx + 80, ay + 28), fill=PINK)
            d.rectangle((sx + 54, ay + 28, sx + 76, ay + 42), fill=PAPER, outline=PINK)
        d.text((sx + 110, ay + 14), label,
               font=f(20, True if highlighted else False),
               fill=PINK if highlighted else TEXT)
        ay += 70

    # arrow + callout outside the phone
    arrow(d, fx + fw + 10, sy + 470, color=PINK, size=40)
    d.text((fx + fw + 100, sy + 442), "Tap Print", font=f(28, True), fill=PINK)
    d.text((fx + fw + 100, sy + 478), "then pinch out", font=f(22), fill=PAPER)
    d.text((fx + fw + 100, sy + 506), "on the preview.", font=f(22), fill=PAPER)

    img.save(f"{OUT}/iphone-share-sheet.png")


# ---------- 4. PDF document icon for hero ----------
def pdf_icon():
    W, H = 600, 700
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # paper
    d.rounded_rectangle((60, 80, W - 60, H - 60), radius=20,
                        fill=PAPER, outline=PURPLE, width=4)
    # folded corner
    d.polygon([(W - 60 - 80, 80), (W - 60, 80), (W - 60, 160)],
              fill=YELLOW, outline=PURPLE)
    d.polygon([(W - 60 - 80, 80), (W - 60, 160), (W - 60 - 80, 160)],
              fill=(0xFF, 0xE9, 0x6E))
    # "PDF" badge
    d.rounded_rectangle((110, H - 220, W - 110, H - 130), radius=12, fill=PINK)
    d.text((W // 2 - 55, H - 207), "PDF", font=f(60, True), fill=PAPER)
    # mock text lines
    for i, w in enumerate([300, 380, 260, 340, 300]):
        y = 220 + i * 38
        d.rounded_rectangle((110, y, 110 + w, y + 16), radius=4,
                            fill=(0xC8, 0xC8, 0xCE))

    img.save(f"{OUT}/pdf-icon.png")


# ---------- 5. Multi-image-to-one-PDF illustration ----------
def multi_pdf():
    W, H = 1200, 600
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # three photo squares on the left
    photos = [(80, 100, PINK), (160, 180, PURPLE), (240, 260, YELLOW)]
    for x, y, col in photos:
        d.rounded_rectangle((x, y, x + 240, y + 240),
                            radius=12, fill=col, outline=PAPER, width=4)

    # arrow pointing right (photos → PDF)
    ax = 560
    ay = 400
    sz = 80
    d.polygon([
        (ax + sz + 30, ay),
        (ax + 30, ay - sz // 2),
        (ax + 30, ay - 14),
        (ax, ay - 14),
        (ax, ay + 14),
        (ax + 30, ay + 14),
        (ax + 30, ay + sz // 2),
    ], fill=PAPER)

    # combined PDF on right
    d.rounded_rectangle((780, 100, 1100, 500), radius=18, fill=PAPER,
                        outline=PURPLE, width=4)
    d.polygon([(1020, 100), (1100, 100), (1100, 180)], fill=YELLOW,
              outline=PURPLE)
    d.rounded_rectangle((820, 360, 1060, 440), radius=10, fill=PINK)
    d.text((895, 376), "PDF", font=f(40, True), fill=PAPER)
    for i, w in enumerate([200, 240, 180]):
        y = 220 + i * 36
        d.rounded_rectangle((820, y, 820 + w, y + 14), radius=4,
                            fill=(0xC8, 0xC8, 0xCE))

    img.save(f"{OUT}/multi-to-one.png")


if __name__ == "__main__":
    windows_dialog()
    mac_dialog()
    iphone_share()
    pdf_icon()
    multi_pdf()
    print("Wrote 5 illustrations to", OUT)
