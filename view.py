# Importando SQLite

import sqlite3 as lite

# Criando a conexão com o banco
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# Tabela de cursos ------------------------------------------

# Criar cursos

def criar_cursos(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cursor.execute(query, i)

#criar_cursos(['Python', '2 semanas', 50.0])

# Ver todos os cursos

def ver_cursos():
    lista = []
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM cursos")
        linha = cursor.fetchall()
        for i in linha:
            lista.append(i)
    return lista


#print(ver_cursos())

# Atualizar cursos

def atualizar_cursos(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id = ?"
        cursor.execute(query, i)

# l = ['Python', '4 semanas', 75.8, 1]    
# print(atualizar_cursos(l))

# print(ver_cursos())


# Deletar cursos

def deletar_cursos(id):
    with con:
        cursor = con.cursor()
        query = "DELETE from cursos WHERE id = ?"
        cursor.execute(query, id)

#l = [1]    

#deletar_cursos(l)
#print(ver_cursos())
