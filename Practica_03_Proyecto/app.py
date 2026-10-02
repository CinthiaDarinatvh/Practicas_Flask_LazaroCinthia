from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    area = None
    perimetro = None
    if request.method == "POST":
        base = float(request.form["base"])
        altura = float(request.form["altura"])
        area = base * altura
        perimetro = 2 * (base + altura)
    return render_template("rectangulo.html", area=area, perimetro=perimetro)

if __name__ == "__main__":
    app.run(debug=True)