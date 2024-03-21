# -*- coding: utf-8 -*-
"""QR Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10RkqoezuMlhDVRRuPQeFoysUUN5xtP4a
"""

!pip install qrcode

import qrcode
from PIL import Image

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.show()

# User input
data = input("Enter the data you want to encode: ")

generate_qr_code(data)