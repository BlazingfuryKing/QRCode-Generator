import os
import qrcode
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
QR_FOLDER = os.path.join('static', 'qr_codes')
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        filename = f"QR_{abs(hash(text))}.png"
        filepath = os.path.join(QR_FOLDER, filename)

        # Generate QR code
        img = qrcode.make(text)
        img.save(filepath)

        return render_template('result.html', filename=filename)
    return render_template('index.html')

@app.route('/qr/<filename>')
def qr_image(filename):
    return send_from_directory(QR_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
