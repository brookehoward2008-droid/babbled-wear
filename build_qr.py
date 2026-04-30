"""Generate a QR code for the sandbox URL, styled in BaBBled colors."""
import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://brookehoward2008-droid.github.io/babbled-wear/sandbox.html"

qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H,
                   box_size=20, border=2)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color=(0x0F, 0x0F, 0x14), back_color=(0xFA, 0xFA, 0xFA))
img.save("img/training/sandbox-qr.png")
print(f"Saved QR for {URL} -> img/training/sandbox-qr.png")
