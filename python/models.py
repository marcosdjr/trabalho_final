#Perguntar o que é essa...

from main import insert, select, update, delete, select_like

#def insert_diretores(nome_completo):
#    insert("diretores",["nome_completo"],[nome_completo])

#def get_diretores(id):
#    select("diretores", "id", id)

#atualizado

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)


#_________________Gêneros

def insert_genero(nome):
    return insert("generos", ["nome"], [nome])

def get_genero(id_genero):
    return select("generos", "id", id_genero)[0]

def update_genero(id_genero, nome):
    update("generos", "id", id_genero, ["nome"], [nome])

def delete_genero(id_genero):
    delete("generos", "id", id_genero)

def select_generos(nome):
    return select_like("generos", "nome", nome)




#_________________Diretor

def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]

def update_diretor(id_diretor, nome_completo):
    update("diretores", "id", id_diretor, ["nome_completo"], [nome_completo])

def delete_diretor(id_diretor):
    delete("diretores", "id", id_diretor)

def select_diretores(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)


#________________Filmes

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]

def update_filme(id_filme,titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def delete_filme(id_usuario):
    delete("filmes", "id", id_filme)

def select_filmes(titulo):
    return select_like("filmes", "titulo", titulo)