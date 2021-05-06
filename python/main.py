from mysql.connector import connect

CONFIGURACOES_BD = {
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"locadora",
}

def execute(sql, params=None):
    """ Executa um comando no mysql e salva os valores
        Serve para: inser, update, delete, create, alter, drop
    """
    with connect(**CONFIGURACOES_BD) as conn: # conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            conn.commit() # grava as coisas no banco de dados
            return cursor.lastrowid
def query(sql, params=None):
    """ Executa um comando no mysql e retorna o resultado
        Serve para: Select, SHOW """
    with connect(**CONFIGURACOES_BD) as conn: #conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            return cursor.fetchall() # pega o resultado da consulta e retorna


#def insert(tabela, colunas, valores):
#    execute(f"INSERT IGNORE INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)

#insert("diretores",["id","nome_completo"],["1","RobertoSantucci"])
#insert("diretores",["id","nome_completo"],["2","JoséPadilha"])
#insert("diretores",["id","nome_completo"],["3","CláudioTorres"])
#insert("diretores",["id","nome_completo"],["4","KátiaLund"])
#insert("diretores",["id","nome_completo"],["5","JorgeFurtado"])
#insert("diretores",["id","nome_completo"],["6","MarcosPaulo"])
#insert("diretores",["id","nome_completo"],["7","JaymeMonjardim"])
#insert("diretores",["id","nome_completo"],["8","MauroLima"])
#insert("diretores",["id","nome_completo"],["9","CaoHamburger"])
#insert("diretores",["id","nome_completo"],["10","WalterSalles"])



def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])


def select(tabela, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} = %s LIMIT {limit} offset {offset}""", (valor_chave,))

#select("estados")
# delete("idiomas", "id", 152)
# insert("idiomas", ["sigla", "nome"], ["ZZ", "Big Brother Brasil"])
# update("idiomas", "id", 152, ["sigla", "nome"], ["ZY", "Big Brother Curitiba"])







