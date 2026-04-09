import qrcode 
import os 

data = input("Enter URL: ")
qr = qrcode.QRCode(
    box_size=10,
    version=1,
    border=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image()
img.save("generatedqr.png")
print("Saved at: ", os.getcwd())
img.show()