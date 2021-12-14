
from tkinter import *
from tkinter import ttk
from cliente_db import *
from animal_db import *

from atendimento_db import *

class IFAtendimento:
    def __init__(self, master=None):

        self.fonte = ("Palatino Linotype", "14")
        self.container1 = Frame(master, bg="grey61")
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master, bg="grey61")
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master, bg="grey61")
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master, bg="grey61")
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master, bg="grey61")
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master, bg="grey61")
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master, bg="grey61")
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master, bg="grey61")
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master, bg="grey61")
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Atendimentos :",fg="#92E3A9", bg="grey61")
        self.titulo["font"] = ("Palatino Linotype", "28", "bold")
        self.titulo.pack ()

        self.lblid = Label(self.container2, text="idAtendimento:", font=self.fonte, width=20, bg="#92E3A9", fg="grey11")
        self.lblid.pack(side=LEFT)

        self.txtid = Entry(self.container2)
        self.txtid["width"] = 10
        self.txtid["font"] = self.fonte
        self.txtid.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10, bg="grey11",fg='White')
        self.btnBuscar["command"] = self.buscarAtentimento
        self.btnBuscar.pack(side=RIGHT)

        self.lblservico = Label(self.container4, text="Serviço: ",font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblservico.pack(side=LEFT)

        self.txtservico = Entry(self.container4)
        self.txtservico["width"] = 25
        self.txtservico["font"] = self.fonte
        self.txtservico.pack(side=LEFT)

        self.lblcliente = Label(self.container5, text="Nome do Cliente: ",
        font=self.fonte, width=20, bg="grey61", fg="white")
        self.lblcliente.pack(side=LEFT)

        self.cliente = Clientes()
        self.dados3 = self.cliente.retornaCliente()
        self.dados3_clientenome = []
        self.dados3_clienteid = []
        for dado in self.dados3:
            self.dados3_clienteid.append(dado[0])
            self.dados3_clientenome.append(dado[1])
#        self.comboProprietario["values"] = self.dados3_clientenome

        self.comboProprietario = ttk.Combobox(self.container5, values=self.dados3_clientenome, state="readonly")
        self.comboProprietario.pack(side=LEFT)
        self.comboProprietario.bind("<<ComboboxSelected>>", self.Proprietario())

        self.lblanimal= Label(self.container6, text="Nome do Animal:",
        font=self.fonte, width=20, bg="grey61", fg="white")
        self.lblanimal.pack(side=LEFT)

        self.animal = Animais()
        self.dados4 = self.animal.retornaAnimal()
        self.dados4_animalnome = []
        self.dados4_animalid = []
        for dado in self.dados4:
             self.dados4_animalid.append(dado[0])
             self.dados4_animalnome.append(dado[1])

        self.comboAnimal = ttk.Combobox(self.container6, values=self.dados4_animalnome, state="readonly")
        self.comboAnimal.pack(side=LEFT)

        self.lblvalor= Label(self.container7, text="Valor Total:",font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblvalor.pack(side=LEFT)

        self.txtvalor = Entry(self.container7)
        self.txtvalor["width"] = 10
        self.txtvalor["font"] = self.fonte
        self.txtvalor.pack(side=RIGHT)

        # Pensei em colocar inserir pra fazer possiveis alterações sem precisar abrir o banco

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntInsert["command"] = self.inserirAtendimento
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntAlterar["command"] = self.alterarAtendimento
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntExcluir["command"] = self.excluirAtendimento
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", bg="grey61", fg="white")
        self.lblmsg["font"] = ("Palatino Linotype", "24", "italic")
        self.lblmsg.pack()


    def Proprietario(self):

        self.cliente = Clientes()
        self.dados3 = self.cliente.retornaCliente()
        self.dados3_clientenome = []
        self.dados3_clienteid = []
        for dado in self.dados3:
            self.dados3_clienteid.append(dado[0])
            self.dados3_clientenome.append(dado[1])
        self.comboProprietario["values"] = self.dados3_clientenome

    def alterarAtendimento(self):
        ATD = Atendimento()

        ATD.id = self.txtid.get()
        ATD.cliente_id = self.dados3_clienteid[self.dados3_clientenome.index(self.comboProprietario.get())]
        ATD.animal_id = self.dados4_animalid[self.dados4_animalnome.index(self.comboAnimal.get())]
        ATD.servico = self.txtservico.get()
        ATD.valor = self.txtvalor.get()

        self.lblmsg["text"] = ATD.alterarAtendimento()

        self.txtid.delete(0, END)
        self.comboProprietario.set("")
        self.comboAnimal.set("")
        self.txtservico.delete(0, END)
        self.txtvalor.delete(0, END)

    def excluirAtendimento(self):
        ATD = Atendimento()
        ATD.id = self.txtid.get()
        self.lblmsg["text"] = ATD.excluirAtendimento()
        self.txtid.delete(0, END)
        self.txtservico.delete(0, END)
        self.comboProprietario.delete("")
        self.comboAnimal.delete("")
        self.txtvalor.delete(0, END)

    def buscarAtentimento(self):
        ATD = Atendimento()
        ATD.id = self.txtid.get()
        self.lblmsg["text"] = ATD.selecionaAtendimento()
        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, ATD.id)
        self.txtservico.delete(0, END)
        self.txtservico.insert(INSERT, ATD.servico)
        self.comboProprietario.set(ATD.cliente_nome)
        self.comboAnimal.set(ATD.animal_nome)
        self.txtvalor.delete(0, END)
        self.txtvalor.insert(INSERT,ATD.valor)

    # Pensei em colocar inserir pra fazer possiveis alterações sem precisar abrir o banco

    def inserirAtendimento(self):
        ATD = Atendimento()
        ATD.cliente_id = self.dados3_clienteid[self.dados3_clientenome.index(self.comboProprietario.get())]
        ATD.animal_id = self.dados4_animalid[self.dados4_animalnome.index(self.comboAnimal.get())]
        ATD.servico = self.txtservico.get()
        ATD.valor = self.txtvalor.get()
        self.lblmsg["text"] = ATD.inserirAtendimento()
        self.txtservico.delete(0, END)
        self.txtvalor.delete(0, END)
        self.comboAnimal.set("")
        self.comboProprietario.set("")





