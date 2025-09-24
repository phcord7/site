from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tabuada = []
    numero = None

    if request.method == "POST":
        try:
            numero = int(request.form["numero"])
            for i in range(1, 101):
                tabuada.append(f"{numero} x {i} = {numero * i}")
        except:
            tabuada = ["Digite um número válido."]

    return render_template("index.html", tabuada=tabuada, numero=numero)

if __name__ == "__main__":
    app.run(debug=True)
