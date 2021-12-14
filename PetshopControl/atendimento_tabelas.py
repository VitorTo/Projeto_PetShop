from tkinter import ttk
from tkinter import *

import MainTeste
from atendimento_db import *



class TabelaServicos:
    def __init__(self, master=None):
        self.fonte= ("Palatino Linotype", "14")

        self.lblTabela = Label(master, text="histórico de serviço", font=self.fonte, width=20, bg="#92E3A9", fg="grey11")
        self.lblTabela.place(x=1010,y=25)

        self.lblTabela2 = Label(master, text="histórico de clientes", font=self.fonte, width=20, bg="#92E3A9", fg="grey11")
        self.lblTabela2.place(x=100, y=25)


        ATENDIMENTO=Atendimento()
        dados=ATENDIMENTO.retornarValor()

        tree = ttk.Treeview(master,height=15,column=("column1","column2","column3"),show='headings')
        tree.column("#1", width=75, anchor="center")
        tree.column("#2", width=100, anchor="center")
        tree.column("#3", width=75, anchor="center")
        tree.heading("#1", text="NOME")
        tree.heading("#2", text="SERVIÇO")
        tree.heading("#3", text="VALOR")
        for dados in dados:
            tree.insert('','end',values=dados)
        tree.place(x=1000, y=55)

        self.button = Button(master, text= "Atualiza ",bg="#92E3A9",fg="grey11", command= self.Atualiza()).pack(pady=10,padx=5, side=LEFT)

        ATDS = Atendimento()
        dados2 = ATDS.retornarNome()

        tree2 = ttk.Treeview(master, height=15, column=("column1", "column2"), show='headings')
        tree2.column("#1", width=110, anchor="center")
        tree2.column("#2", width=110, anchor="center")

        tree2.heading("#1", text="NOME")
        tree2.heading("#2", text="ID")

        for dados2 in dados2:
            tree2.insert('', 'end', values=dados2)
        tree2.place(x=100, y=55)
    # Mostrar id, nome

    class Atualiza():

        def retorna(self):

            return Atendimento





