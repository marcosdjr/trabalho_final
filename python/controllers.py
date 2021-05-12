from flask import Flask, jsonify, request
from datetime import datetime
from main import query, execute
from decimal import Decimal
from models import insert_genero, get_genero, update_genero, delete_genero, select_generos
from models import insert_diretor, get_diretor, update_diretor, delete_diretor, select_diretores
from models import insert_usuario, get_usuario, update_usuario, delete_usuario, select_usuarios
from models import insert_filme, get_filme, update_filme, delete_filme, select_filmes
from models import insert_locacao, get_locacao, update_locacao, delete_locacao, select_locacao
from models import insert_pagamento, get_pagamento


from serializadores import usuario_from_web, usuario_from_db,  nome_usuario_from_web
from serializadores import genero_from_web, genero_from_db, nome_genero_from_web
from serializadores import diretor_from_web, diretor_from_db,  nome_diretor_from_web
from serializadores import filme_from_web, filme_from_db,  titulo_filme_from_web
from serializadores import locacao_from_web, locacao_from_db,  id_locacao_from_web
from serializadores import pagamento_from_web, pagamento_from_db,  id_pagamento_from_web

from validacao import valida_usuario, valida_genero, valida_diretor, valida_filme, valida_locacao


app = Flask(__name__)

#Usuários
@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido. Verifique as informações digitadas."})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido. Verifique as informações digitadas."})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


#Gêneros
@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Gênero inválido. Verifique as informações digitadas."})

@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Gênero inválido. Verifique as informações digitadas."})

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return "", 204
    except:
        return jsonify({"erro": "Gênero possui itens conectados a ele"})

@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome = nome_genero_from_web(**request.args)
    generos = select_generos(nome)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)



#Diretores
@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor inválido. Verifique as informações digitadas."})

@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor inválido. Verifique as informações digitadas."})

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return "", 204
    except:
        return jsonify({"erro": "Diretor possui itens conectados a ele"})

@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    nome_completo= nome_diretor_from_web(**request.args)
    diretores = select_diretores(nome_completo)
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db)

#Filmes
@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme inválido. Verifique as informações digitadas."})

@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme inválido. Verifique as informações digitadas."})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return "", 204
    except:
        return jsonify({"erro": "Filme possui itens conectados a ele"})

@app.route("/filmes", methods=["GET"])
def buscar_filme():
    titulo = titulo_filme_from_web(**request.args)
    filmes = select_filmes(titulo)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

#Locações
@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)  # 3 - formata o que vem da internet
    pag = pagamento_from_web(**request.json)
    if valida_locacao(**locacao):
        id_locacao = insert_locacao(**locacao)
        #get_locacao(id_locacao)
        insert_pagamento(id_locacao, **pag)
        loc = select_locacao(id_locacao)

        return jsonify(locacao_from_db(loc))
    else:
        return jsonify({"erro": "Locação inválida. Verifique as informações digitadas."})

@app.route("/locacoes/<int:id>", methods=["PUT", "PATCH"])
def alterar_locacao(id):
    locacao = locacao_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_locacao(**locacao):
        update_locacao(id, **locacao)
        locacao_cadastrada = get_locacao(id)
        return jsonify(locacao_from_db(locacao_cadastrada))
    else:
        return jsonify({"erro": "Filme inválido. Verifique as informações digitadas."})

@app.route("/locacoes/<int:id>", methods=["DELETE"])
def apagar_locacao(id):
    try:
        delete_locacao(id)
        return "", 204
    except:
        return jsonify({"erro": "Locação possui itens conectados a ela"})

@app.route("/locacoes", methods=["GET"])
def buscar_locacao():
    id = id_locacao_from_web(**request.args)
    locacoes = select_locacoes(id)
    locacoes_from_db = [locacao_from_db(locacao) for locacao in locacoes]
    return jsonify(locacoes_from_db)


#Fazer uma locação => enviar id_filme, id_usuario, tipo_pagamento, data_inicio
# Criar um pagamento, junto com a locação
# Colocar a data de fim 48h depois da data de inicio (automático)
# Preencher o valor do pagamento com o valor do filme
# Gerar um código de pagamento aleatório pra preencher no código de pagamento
# Colocar o status aleatório


#Pagamento














#Deixar isso sempre por último
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)