from tkinter import ttk
from tkinter import *
from genero_especie_db import GenerosEspecies

class IFGeneroEspecie:
    def __init__(self, master=None):
        genero=GenerosEspecies()
        dados=genero.retornarGenerosEspecies()
        tree = ttk.Treeview(master,height=20,column=("column1","column2"),show='headings')
        tree.heading("#1", text="GÊNERO")
        tree.heading("#2", text="ESPÉCIE")
        for dados in dados:
            tree.insert('','end',values=dados)
        tree.pack()
