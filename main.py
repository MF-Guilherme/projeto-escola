from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

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

janela.mainloop()