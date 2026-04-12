from flask import Flask, request, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", show_qr=False)

@app.route("/generate", methods=["POST"])
def generate():
    #fetching the inputted values from html form 
    data = request.form["data"]
    fill_color = request.form["fill-color"]
    back_color = request.form["back-color"]

    #creating qr using QRCode object
    qr = qrcode.QRCode(border = 2, box_size= 3)
    qr.add_data(data)
    qr.make(fit=True)

    #making image of the qr with the custom colour
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save("static/your-qr.png")
    return render_template("index.html", show_qr=True)

app.run(debug=True)
