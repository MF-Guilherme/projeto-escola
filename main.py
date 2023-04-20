from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image

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
    print('Aluno')


# Função para adicionar Cursos e Turmas
def adicionar():
    print('Cursos e turmas')


# Função para salvar
def salvar():
    print('Salvar')


# Função de controle ------------------------
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



# Criando botões

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



janela.mainloop()