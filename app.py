from flask import Flask, request, render_template, send_from_directory
import qrcode
import os
import re

app = Flask(__name__)

# QRコードの保存先ディレクトリ
QR_CODE_DIR = 'static/qr_codes'
os.makedirs(QR_CODE_DIR, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    
    # 不正な文字を取り除くための関数
    def sanitize_filename(filename):
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    qr_filename = f"{sanitize_filename(data)}.png"
    qr_path = os.path.join(QR_CODE_DIR, qr_filename)

    # QRコードを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)

    # 生成したQRコードのパスを相対パスにして渡す
    qr_code_path = f"/static/qr_codes/{qr_filename}"
    return render_template('index.html', qr_code_path=qr_code_path)

if __name__ == '__main__':
    app.run(debug=True)
