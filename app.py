from flask import Flask, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    # シンプルなフォームを返す
    return '''
        <form action="/generate" method="post">
            <input type="text" name="data" placeholder="QRコードにしたいデータ">
            <button type="submit">生成</button>
        </form>
    '''

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    
    # QRコード生成
    qr_img = qrcode.make(data)
    qr_img.save("qr_code.png")
    
    # 生成されたQRコード画像を返す
    return send_file("qr_code.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True, port=10000)
