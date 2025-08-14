from exemplo.main import app # agora nesse novo arquivo nao tem mais o app entao tem que importar
from flask import render_template

@app.route("/inicio")
def homepage():
    return render_template("homepage.html")
