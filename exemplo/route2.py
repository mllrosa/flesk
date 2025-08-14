from exemplo.main import app # agora nesse novo arquivo nao tem mais o app entao tem que importar

@app.route("/blog")
def blog():
    return "meu blog"
