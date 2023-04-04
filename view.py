# Importando SQLite

import sqlite3 as lite

# Criando a conexão com o banco
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com banco de dados:", e)

# Tabela de cursos ------------------------------------------

# Criar curso

def criar_curso(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cursor.execute(query, i)
        print("Curso criado com sucesso!")

#criar_curso(['Python', '2 semanas', 50.0])

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


# print(ver_cursos())

# Atualizar curso

def atualizar_curso(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id = ?"
        cursor.execute(query, i)
        print("Curso atualizado com sucesso!")

# l = ['Python', '4 semanas', 75.8, 2]    
# print(atualizar_curso(l))

# print(ver_cursos())


# Deletar curso

def deletar_curso(id):
    with con:
        cursor = con.cursor()
        query = "DELETE from cursos WHERE id = ?"
        cursor.execute(query, id)
        print("Curso deletado com sucesso")

#l = [1]    

#deletar_curso(l)
#print(ver_cursos())


# Tabela de Turmas -------------------------------------------------------

# Criar turmas
def criar_turma(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cursor.execute(query, i)
        print("Turma criada com sucesso")

# l = ["2A", "Java", "2023-10-29"]
# print(criar_turma(l))

# Ver todas as turmas
def ver_turmas():
    lista = []
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM turmas")
        linha = cursor.fetchall()
        for i in linha:
            lista.append(i)
    return lista

print(ver_turmas())

# Atualizar turma
def atualizar_turma(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cursor.execute(query,i)
        print("Dados atualizados com sucesso!")

# l = ["2B", "Python", "2023-10-29", 2]
# print(atualizar_turma(l))

# Deletar turma
def deletar_turma(id):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM turmas WHERE id=?"
        cursor.execute(query, id)
        print("Turma deletada com sucesso")

# l = [2]
# print(deletar_turma(l))