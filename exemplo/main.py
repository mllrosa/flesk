from flask import Flask

# app no caso é o site em si, ele chama esse site de app
app = Flask(__name__) # name é como se fosse o nome do arquivo e a forma padrao de criar um aplicativo no flask

# criar rotas
# @app.route("/inicio")
# def homepage():
#     return "meu site" # ja a API devolveria json, arquivo e outros

# isso serve pra coisas simples mas geralmente as rotas saofeitas em outros arquivos e chamamos elas aqui 

from exemplo.route1 import * # * importar todas as coisas

from exemplo.route2 import *

# executar o site e colocar no ar
if __name__ == "__main__": # so vai executar esse codigo quando eu estiver executando esse arquivo diretamente
    app.run()