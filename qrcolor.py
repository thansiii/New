import qrcode
def qr(data,color,bg,filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color,back_color=bg)
    img.save(f"{filename}.png")
    print("QR Successfully created")

data = input("Enter The Content To Put Inside Qr")   
color = input("Enter The color for Qr")
bg = input("Enter the color for bg")
filename = input("Enter the name for the Qr")
qr(data,color,bg,filename)