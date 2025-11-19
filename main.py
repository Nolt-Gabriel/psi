from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index (): 

    return render_template("dashboard.html")

@app.route("/Comprar Créditos")
def comprar():

    return render_template("compras.html")

if __name__ == "__main__":

    app.run()
