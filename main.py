from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date

cor0 = '#2e2d2b' # Preto
cor1 = '#feffff' # Branco
cor2 = '#e5e5e5' # Grey
cor3 = '#00a095' # Verde
cor4 = '#403d3d' # letra
cor5 = '#003452' # azul
cor7 = '#ef5350' # vermelho

cor6 = '#038cfc' # azul
cor8 = '#263238' # + verde
cor9 = '#e9edf5' # + verde

# Criando janela vazia

janela = Tk()
janela.title('')
janela.geometry('850x620')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')


# Criando frames
frame_logo = Frame(janela, width=850, height=52, bg=cor6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=cor1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg= cor1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg= cor1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


# Trabalhando no frame logo------------
logo = Image.open(r'./icons/student.png')
logo = logo.resize((50,50))
logo = ImageTk.PhotoImage(logo)
label_logo = Label(frame_logo, image=logo, text='Cadastro de Alunos', width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
label_logo.place(x=0, y=0)

# função para cadastrar alunos
def alunos():
    
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify=LEFT, relief=SOLID)
    e_nome.place(x=7, y=40)

    l_email = Label(frame_detalhes, text="E-mail *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_email.place(x=4, y=70)
    e_email = Entry(frame_detalhes, width=45, justify=LEFT, relief=SOLID)
    e_email.place(x=7, y=100)

    l_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_telefone.place(x=4, y=130)
    e_telefone = Entry(frame_detalhes, width=20, justify=LEFT, relief=SOLID)
    e_telefone.place(x=7, y=160)
    
    l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_sexo.place(x=190, y=130)

    cb_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    cb_sexo['values'] = ('Masculino', 'Feminino')
    cb_sexo.place(x=190, y=160)

    l_data_nascimento = Label(frame_detalhes, text='Data de Nascimento *', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_data_nascimento.place(x=446, y=10)
    data_nacimento = DateEntry(frame_detalhes, width=18, background = 'darkblue', foreground='white', borderwidth=2, year=2023 )
    data_nacimento.place(x=450, y=40)

    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify=LEFT, relief=SOLID)
    e_cpf.place(x=450, y=100)

    # Pegando as turmas
    turmas = ['Python Turma A', 'Python Turma B']
    turma = []

    for i in turmas:
        turma.append(i)

    l_curso = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_curso.place(x=446, y=130)    
    cb_turma = ttk.Combobox(frame_detalhes, width=18, font=('Ivy 8 bold'))
    cb_turma['values'] = (turma)
    cb_turma.place(x=450, y=160)
    

# Função para adicionar Cursos e Turmas
def adicionar():
    # Criando frames para tabelas
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=cor1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=cor1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=cor1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    # Detalhes do curso ---------------------------------------------------------------

    l_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify=LEFT, relief=SOLID)
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify=LEFT, relief=SOLID)
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify=LEFT, relief=SOLID)
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='SALVAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor3, fg=cor1)
    botao_carregar.place(x=107, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='ATUALIZAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor6, fg=cor1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='DELETAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor7, fg=cor1)
    botao_deletar.place(x=267, y=160)

    # Tabela de Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scroolbars
        list_header = ['ID', 'Curso', 'Duração', 'Preço']

        df_list = []

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode='extended', columns=list_header, show='headings')
        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient='vertical', command=tree_curso.yview)
        # horizontal scrollbar        
        hsb = ttk.Scrollbar(frame_tabela_curso, orient='horizontal', command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_curso.grid(column=0, row=1, sticky=NSEW)
        vsb.grid(column=1, row=1, sticky=NS)
        hsb.grid(column=0, row=2, sticky=EW)
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_curso.column(col, width=h[n], anchor=hd[n])

            n+=1
        
        for item in df_list:
            tree_curso.insert('end', values=item)
        
    mostrar_cursos()

    # linha separatória parte de cima----------------------

    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=cor0, fg=cor0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=cor1, fg=cor0)
    l_linha.place(x=372, y=10)

    # linha separatória parte de baixo (tabela) ----------------------

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=cor0, fg=cor0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=cor1, fg=cor0)
    l_linha.place(x=4, y=10)

    # detalhes da turma -----------------------------------------------

    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify=LEFT, relief=SOLID)
    e_nome_turma.place(x=407, y=40)

    l_curso = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_curso.place(x=404, y=70)
    
    # Pegando os cursos
    cursos = ['curso 1', 'curso 2']
    curso = []

    for i in cursos:
        curso.append(i)
    
    cb_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    cb_curso['values'] = (curso)
    cb_curso.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text='Data de Início', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background = 'darkblue', foreground='white', borderwidth=2, year=2023 )
    data_inicio.place(x=407, y=160)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='SALVAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor3, fg=cor1)
    botao_carregar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='ATUALIZAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor6, fg=cor1)
    botao_atualizar.place(x=587, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='DELETAR', width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor7, fg=cor1)
    botao_deletar.place(x=667, y=160)

    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scroolbars
        list_header = ['ID', 'Nome da Turma', 'Curso', 'Início']

        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode='extended', columns=list_header, show='headings')
        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient='vertical', command=tree_turma.yview)
        # horizontal scrollbar        
        hsb = ttk.Scrollbar(frame_tabela_turma, orient='horizontal', command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_turma.grid(column=0, row=1, sticky=NSEW)
        vsb.grid(column=1, row=1, sticky=NS)
        hsb.grid(column=0, row=2, sticky=EW)
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 130, 150, 80]
        n = 0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_turma.column(col, width=h[n], anchor=hd[n])

            n+=1
        
        for item in df_list:
            tree_turma.insert('end', values=item)
        
    mostrar_turmas()


# Função para salvar
def salvar():
    print('Salvar')


# Função de controle --------------------------------
def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # chamando a função aluno
        alunos()
    elif i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # chamando a função adicionar
        adicionar()
    else:
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # chamando a função salvar
        salvar()


# Criando botões -------------------------------------

#botão de cadastro
app_img_cadastro = Image.open(r'./icons/add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
btn_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text='Cadastro', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
btn_cadastro.place(x=10, y=30)

#botão de adicionar
app_img_adicionar = Image.open(r'./icons/add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
btn_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_cadastro, text='Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
btn_adicionar.place(x=123, y=30)

#botão de cadastro
app_img_salvar = Image.open(r'./icons/save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
btn_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text='Salvar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
btn_salvar.place(x=236, y=30)


alunos()
janela.mainloop()