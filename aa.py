from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "minha_chave_secreta"  # necessário para usar sessão

@app.route("/", methods=["GET", "POST"])
def home():
    # Gera o número secreto se ainda não existir
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 50)

    mensagem = ""
    if request.method == "POST":
        palpite = int(request.form["palpite"])
        numero = session["numero_secreto"]

        if palpite < numero:
            mensagem = "Muito baixo!"
        elif palpite > numero:
            mensagem = "Muito alto!"
        else:
            mensagem = f"Acertou! O número era {numero}."
            session.pop("numero_secreto")  # reseta o jogo

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)