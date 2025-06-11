#pip install qrcode
import qrcode

#generate qr code
img = qrcode.make('91605930')

#save the image as an image file like (.jpg)
img.save('Luge.jpg')