import qrcode

url_link = input("Enter the URL to generate Qrcode: ")
file_name = input("Enter the file name: ")
file_name = f"{file_name}.png"

qr = qrcode.QRCode(box_size = 10, border = 5, version = 1)
qr.add_data(url_link)
qr.make()

qr_img = qr.make_image(fill_color = "black", back_color = "white")
qr_img.save(file_name)
print("Qr code generated successfully!")
