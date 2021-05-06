from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal


app = Flask(__name__)

#@app.route("/", methods=["GET", "POST"])
#def hello():
#    if request.method == "GET":
#        return jsonify(query("SHOW schemas"))
#    elif request.method == "POST":
#        return request.json

#@app.route("/usuarios", methods=["POST"])
#def login():
#    email = request.json["email"]
#    senha = request.json["senha"]
#    return jsonify(query(f"SELECT * FROM usuarios WHERE email = %s and senha=%s", (email, senha)))

def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])

def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)

def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))

#Inserir diretores
@app.route("/diretores", methods=["POST"])
def inserir_diretores():
    nome_completo = request.json["nome"]

    insert("diretores" , ["nome_completo"] , [nome_completo])
    return jsonify(query("SELECT * FROM diretores"))

#Inserir usuarios
@app.route("/usuarios", methods=["POST"])
def inserir_usuarios():
    nome_completo = request.json["nome"]
    cpf = request.json["cpf"]

    insert("usuarios" , ["nome_completo" , "cpf"] , [nome_completo, cpf,])
    return jsonify(query("SELECT * FROM usuarios"))

#Inserir gêneros
@app.route("/generos", methods=["POST"])
def inserir_generos():
    nome = request.json["nome"]

    insert("generos" , ["nome"] , [nome])
    return jsonify(query("SELECT * FROM generos"))

#Inserir Filme
@app.route("/filmes", methods=["POST"])
def inserir_filmes():
    titulo = request.json["titulo"]
    ano = request.json["ano"]
    classificacao = request.json["classificacao"]
    preco = request.json["preco"]
    diretores_id = request.json["diretores_id"]
    generos_id = request.json["generos_id"]

    insert("filmes", ["titulo", "ano" , "classificacao" , "preco" , "diretores_id" , "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id, ])
    return jsonify(query("SELECT * FROM filmes"))

#Alterar diretores
@app.route("/diretores/<int:id>", methods=["PUT"])
def diretores(id):
    nome_completo = request.json["nome"]

    update("diretores", "id", id, ["nome_completo"],[nome_completo])
    return jsonify(query("SELECT * FROM diretores WHERE id = %s",(id,)))

#Alterar usuarios
@app.route("/usuarios/<int:id>", methods=["PUT"])
def usuarios(id):
    nome_completo = request.json["nome"]
    cpf = request.json["cpf"]

    update("usuarios", "id", id, ["nome_completo" , "cpf"],[nome_completo , cpf])
    return jsonify(query("SELECT * FROM usuarios WHERE id = %s",(id,)))

#Alterar gêneros
@app.route("/generos/<int:id>", methods=["PUT"])
def generos(id):
    nome = request.json["nome"]

    update("generos", "id", id, ["nome"],[nome])
    return jsonify(query("SELECT * FROM generos WHERE id = %s",(id,)))

#Deletar diretores
@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretores(id):
    delete("diretores", "id", id)
    # none, 204 = sem conteúdo
    return (None, 204)

#Deletar usuarios
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuarios(id):
    delete("usuarios", "id", id)
    # none, 204 = sem conteúdo
    return (None, 204)

#Deletar generos
@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_generos(id):
    delete("generos", "id", id)
    #none, 204 = sem conteúdo
    return (None, 204)


#Buscar Diretores
@app.route("/diretores", methods=["GET"])
def listar_diretores():
    #Para o método GET, usar o request.args, e no Insomnia, usar a aba query, não a json.
    nome_completo = request.args["nome"]
    if nome_completo == "todos":
        return jsonify(query("SELECT * FROM diretores"))
    else:
        return jsonify(query("SELECT * FROM diretores WHERE nome_completo LIKE %s", (nome_completo,)))

#Buscar Usuarios
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    #Para o método GET, usar o request.args, e no Insomnia, usar a aba query, não a json.
    nome_completo = request.args["nome"]
    if nome_completo == "todos":
        return jsonify(query("SELECT * FROM usuarios"))
    else:
        return jsonify(query("SELECT * FROM usuarios WHERE nome_completo LIKE %s", (nome_completo,)))

#Buscar Gêneros
@app.route("/generos", methods=["GET"])
def listar_generos():
    #Para o método GET, usar o request.args, e no Insomnia, usar a aba query, não a json.
    nome = request.args["nome"]
    if nome == "todos":
        return jsonify(query("SELECT * FROM generos"))
    else:
        return jsonify(query("SELECT * FROM generos WHERE nome LIKE %s", (nome,)))


#diretores = query("SELECT from diretores where nome LIKE '%s';")
#print(estados)
#update("generos", "id", id, ["nome"],[nome])



#@app.route("/idiomas/<int:id>", methods=["PUT"])
#def idiomas(id):
#    sigla = request.json["sigla"]
#    nome = request.json["nome"]

#    update("idiomas", "id", id, ["sigla", "nome"],[sigla, nome])

#    return jsonify(query("SELECT * FROM idiomas WHERE id = %s",(id,)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


















@app.route("/paises", methods=["GET", "POST"])
def search_paises():
    return jsonify(query("select * from paises"))

#@app.route("/produtos_disponiveis")
#def search_produtos():
#    return jsonify(query("""select produtos.id, produtos.nome, produtos.descricao, produtos.preco from produtos
#                            inner join estoques on estoques.id_produto_estoque = produtos.id where estoques.quantidade > 0"""))



@app.route("/estados/<int:id>", methods=["PUT"])
def alter_estado(id):
   sigla = request.json["sigla"]
   nome = request.json["nome"]

   execute("UPDATE estados SET nome = %s , sigla = %s", (nome,sigla))
   return jsonify(query("select * from estados WHERE id = %s", [id,]))

#Toda vez, o parâmetro final (id) deve estar dentro de uma tupla ou lista. Se tupla, deve ter uma vírgula antes de fechar o parenteses.
#sempre que fizer put, post ou path, requisição tem corpo
#alter_estado('Santa Catarina', 'SC', 1)

#def produtos():
 #   produtos = [(p[0], p[1], p[2], str(p[3])) for p in query("SELECT * FROM produtos" )]

#print (produtos())



#Deixar isso sempre por último
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)