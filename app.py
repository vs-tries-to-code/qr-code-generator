from flask import Flask, request, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.form["data"]
    qr = qrcode.QRCode(
        border = 2,
        box_size= 3,
        )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("static/your-qr.png")
    return "QR successfully generated!"

app.run(debug=True)
