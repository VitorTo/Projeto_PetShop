import tkinter as tk
from tkinter import *
from tkinter import ttk

from atendimento import IFAtendimento
from cliente import *
from animal import IFAnimal
from genero_especie import *
from geral import Geral
#from atendimento import IFAtendimento
#from atendimento_tabelas import TabelaServicos


fonte = ("Palatino Linotype", "13")

# Tentando abrir tab no event de clicar no tab, não consegui
# def abrirTab_selected(event):
#     selected_tab = event.widget.select()
#     tab_text = event.widget.tab(selected_tab, "text")
#
#     if tab_text == "Atendimento":
#         tabControl.add(tab5, text='Atendimento')
#
#     if tab_text == "Clientes":
#         tabControl.add(tab2, text='Clientes')
#
#     if tab_text == "Animais":
#         tabControl.add(tab3, text='Animais')
#
#     if tab_text == 'Espécies X Gêneros':
#         tabControl.add(tab4, text='Espécies X Gêneros')

#tabControl.bind ("<<NotebookTabChanged>>", abrirTab_selected)


root = tk.Tk()
root.title("PetShopControl")
root.bg="#92E3A9"
root.iconbitmap("image/PetIcon.ico")
root.geometry('1300x650')

tabControl = ttk.Notebook(root)
tabControl.pack(pady=10)

def hide():
    tabControl.hide(2)
    tabControl.hide(3)
    tabControl.hide(4)

# def show():
#     tabControl.add(tab5, text="Atendimento")

def select():
    tabControl.select(4)
    tabControl.select(3)
    tabControl.select(2)

def select1():
    tabControl.select(0)

def selectAt():
    tabControl.select(1)

#def Atualiza():
    #Clientes.mainloop()

tab1 = Frame(tabControl, bg="grey61")
tabControl.add(tab1, text="Bem-vindo")
Geral(tab1)

tab5 = Frame(tabControl, bg="grey61")
tabControl.add(tab5, text='Atendimento')
tabControl.pack(expand=1, fill="both")
IFAtendimento(tab5)
#TabelaServicos(tab5)


tab2 = Frame(tabControl, bg="grey61")
tabControl.add(tab2, text='Clientes')
tabControl.pack(expand=1, fill="both")
IFClientes(tab2)

tab3 = Frame(tabControl,bg="grey61")
tabControl.add(tab3, text='Animais')
tabControl.pack(expand=1, fill="both")
IFAnimal(tab3)

tab4 = Frame(tabControl,bg="grey61")
tabControl.add(tab4, text='Espécies X Gêneros')
IFGeneroEspecie(tab4)

# Esconde os tabs mantendo somente o atendimento e principal
btn =Button(tab1, text= "Esconder ",bg="grey11",fg="#92E3A9",font=fonte,width=10, command= hide).pack(pady=10, padx=5, side=LEFT)
# Vai levar direto pra tab principal
btn2 =Button(tabControl, text= "Tela Principal ",bg="#92E3A9",fg="grey11",font=fonte, command= select1).place(x=625, y=542)
# Vai selecionar os tabs que foram escondidos e mudar automaticamente para o cliente
btn3 =Button(tab1, text= "Mostrar ",bg="grey11",fg="#92E3A9",font=fonte, width=10, command= select).pack(pady=10,padx=5, side=LEFT)
# Vai selecionar o tab de atendimento
btn4 =Button(tab1, text= "Atender",bg="grey11",fg="#92E3A9",font=fonte, width=10, command= selectAt).pack(pady=10,padx=5, side=LEFT)

# Tentei iniciar sem precisar fechar o programa, mas não consegui muito bem
#btn5 =Button(tabControl, text= "Atualiza ",bg="#92E3A9",fg="grey11",font=fonte, command= Atualiza).pack(pady=10,padx=5, side=LEFT)



# Geral - página principal - pensei em colocar uma agenda, imagens, gráficos, sei lá... algum para ajudar no dia a dia

tab1 = ttk.Frame(tabControl)
tab1 = Frame(tabControl,bg="grey61")
Geral(tab1)

# Atendimento -
tab5 = ttk.Frame(tabControl)
tab5 = Frame(tabControl, bg="grey61")
tabControl.pack(expand=1, fill="both")
IFAtendimento(tab5)


# cadastro de clientes
tab2 = ttk.Frame(tabControl)
tab2 = Frame(tabControl, bg="grey61")
tabControl.pack(expand=1, fill="both")
IFClientes(tab2)

# cadastro de animais
tab3 = ttk.Frame(tabControl)
tab3 = Frame(tabControl,bg="grey61")
tabControl.pack(expand=1, fill="both")
IFAnimal(tab3)
# gêneros x espécies - treeview
tab4 = ttk.Frame(tabControl)
tab4 = Frame(tabControl,bg="grey61")
IFGeneroEspecie(tab4)


root.mainloop()