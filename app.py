from flask import Flask, request, jsonify
import qrcode
import os

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    img = qrcode.make(data)
    img.save('qr_code.png')
    return jsonify({'message': 'QR code generated!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
