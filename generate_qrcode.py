import qrcode

url = input("Enter the url: ")
file_name = input("Enter the file_name: ")
file_name = f"{file_name}.png"

qr = qrcode.QRCode(border=5, box_size=10)
qr.add_data(url)
qr.make()

img = qr.make_image(fill_color="red", back_color="while")
img.save(file_name)
print("Qrcode was generate successful...")