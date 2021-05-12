
def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True

#_________________________

def valida_genero(nome):
    if len(nome) == 0:
        return False
    else:
        return True

#__________________________

def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False
    else:
        return True

#_________________________

def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):

    if len(titulo) == 0:
        return False


    if len(ano) != 4:
        return False

    if len(classificacao) != 2:
        return False

    if float(preco) > 100.00:
        return False

    if diretores_id == 0:
        return False

    if generos_id == 0:
        return False

    return True

def valida_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return True