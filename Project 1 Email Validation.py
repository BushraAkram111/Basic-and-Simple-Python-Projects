import qrcode
import PIL.Image

def create_qrcode(url):
    """Creates a QR code from the specified URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def print_qrcode(img):
    """Prints the QR code image."""
    img.save("qrcode.png")
    img = PIL.Image.open("qrcode.png")
    img.show()

def main():
    """Prints a QR code from the specified URL."""
    url = input("Enter the URL: ")
    img = create_qrcode(url)
    print_qrcode(img)

if __name__ == "__main__":
    main()
            
