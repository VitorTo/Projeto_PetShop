#from animal_db import Animal
from tkinter import *
from tkinter import ttk
from genero_especie_db import GenerosEspecies
from animal_db import Animais
from cliente_db import Clientes


class IFAnimal:
    def __init__(self, master= None):

        self.container0 = Frame(master, bg="grey61")
        self.container0["pady"] = 10
        self.container0.pack(side=TOP)

        self.fonte = ("Palatino Linotype", "14")
        self.container1 = Frame(master, bg="grey61")
        self.container1["pady"] = 25
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
        self.container7["pady"] = 10
        self.container7.pack()

        self.container8 = Frame(master,bg="grey61")
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master, bg="grey61")
        self.container9["padx"] = 20
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container0, text="Informe os dados: ",width= 40, bg="grey61", fg="#92E3A9")
        self.titulo["font"] = ("Palatino Linotype", "28", "bold")
        self.titulo.pack()

        self.lblidanimal = Label(self.container2, text="idAnimal:",fg="grey11",bg="#92E3A9", font=self.fonte, width=10)
        self.lblidanimal.pack(side=LEFT)

        self.txtidanimal = Entry(self.container2)
        self.txtidanimal["width"] = 10
        self.txtidanimal["font"] = self.fonte
        self.txtidanimal.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",fg="White", font=self.fonte, width=10, bg="grey11")#Z
        self.btnBuscar["command"] = self.buscarAnimal
        self.btnBuscar.pack(side=RIGHT)


        self.lblnome = Label(self.container3, text=" Nome Animal: ",
                             font=self.fonte, width=15, bg="grey61", fg="white")
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblGenero = Label(self.container4, text="Gênero: ", font=self.fonte, width=10, bg="grey61", fg= "White")
        self.lblGenero.pack(side=LEFT)
        self.genero = GenerosEspecies()
        self.dados=self.genero.retornarGeneros()
        self.dados_generodescricao=[]
        self.dados_generoid = []
        for dado in self.dados:
            self.dados_generodescricao.append(dado[1])
            self.dados_generoid.append(dado[0])
        self.comboGenero = ttk.Combobox(self.container4, values=self.dados_generodescricao, state="readonly")
        self.comboGenero.pack()
        self.comboGenero.bind("<<ComboboxSelected>>", self.buscarEspecie)

        self.lblEspecie = Label(self.container5, text="Espécie: ", font=self.fonte, width=10, bg="grey61",fg="White")
        self.lblEspecie.pack(side=LEFT)
        self.comboEspecie = ttk.Combobox(self.container5, values=[], state="readonly")
        self.comboEspecie.pack()

        self.lblraca = Label(self.container6, text="Raça: ",font=self.fonte, width=10, bg="grey61", fg="White")
        self.lblraca.pack(side=LEFT)

        self.txtraca = Entry(self.container6)
        self.txtraca["width"] = 25
        self.txtraca["font"] = self.fonte
        self.txtraca.pack(side=LEFT)

        self.lblProprietario = Label(self.container7, text="Proprietário: ", font=self.fonte, width=10, bg="grey61",fg="white")
        self.lblProprietario.pack(side=LEFT)

        self.cliente = Clientes()
        self.dados2 =self.cliente.retornaCliente()
        self.dados2_clientenome=[]
        self.dados2_clienteid=[]
        for dado in self.dados2:
             self.dados2_clienteid.append(dado[0])
             self.dados2_clientenome.append(dado[1])

        self.comboProprietario = ttk.Combobox(self.container7, values=self.dados2_clientenome, state="readonly")
        self.comboProprietario.pack()
        self.comboProprietario.bind("<<ComboboxSelected>>", self.carregarProprietario())

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntInsert["command"] = self.inserirAnimal
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntAlterar["command"] = self.alterarAnimal
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntExcluir["command"] = self.excluirAnimal
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", bg="grey61", fg="white")
        self.lblmsg["font"] = ("Palatino Linotype", "24", "italic")
        self.lblmsg.pack()

    def buscarEspecie(self,parametro):
        if parametro!="B":
            self.comboEspecie.set("")
        self.genero = GenerosEspecies()
        self.genero.genero_id=self.dados_generoid[self.dados_generodescricao.index(self.comboGenero.get())]
        self.dados = self.genero.retornarEspecies()
        self.dados_especieid=[]
        self.dados_especiedescricao=[]
        for dado in self.dados:
            self.dados_especieid.append(dado[0])
            self.dados_especiedescricao.append(dado[1])
        self.comboEspecie["values"] = self.dados_especiedescricao



    def carregarProprietario(self):

        self.cliente = Clientes()
        self.dados2 = self.cliente.retornaCliente()
        self.dados2_clientenome = []
        self.dados2_clienteid = []
        for dado in self.dados2:
            self.dados2_clienteid.append(dado[0])
            self.dados2_clientenome.append(dado[1])


    def inserirAnimal(self):
        animal = Animais()
        animal.nome = self.txtnome.get()
        animal.raca = self.txtraca.get()
        animal.especie_id = self.dados_especieid[self.dados_especiedescricao.index(self.comboEspecie.get())]
        animal.cliente_id = self.dados2_clienteid[self.dados2_clientenome.index(self.comboProprietario.get())]
        self.lblmsg["text"] = animal.inserirAnimal()
        self.txtnome.delete(0, END)
        self.txtraca.delete(0, END)
        self.comboGenero.set("")
        self.comboEspecie.set("")
        self.comboProprietario.set("")

    def alterarAnimal(self):
        animal = Animais()
        animal.id = self.txtidanimal.get()
        animal.nome = self.txtnome.get()
        animal.raca = self.txtraca.get()
        animal.especie_id = self.dados_especieid[self.dados_especiedescricao.index(self.comboEspecie.get())]
        animal.cliente_id = self.dados2_clienteid[self.dados2_clientenome.index(self.comboProprietario.get())]
        self.lblmsg["text"] = animal.alterarAnimal()
        self.txtidanimal.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtraca.delete(0, END)
        self.comboGenero.set("")
        self.comboEspecie.set("")
        self.comboProprietario.set("")

    def excluirAnimal(self):
        animal = Animais()
        animal.id = self.txtidanimal.get()
        self.lblmsg["text"] = animal.excluirAnimal()
        self.txtidanimal.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtraca.delete(0, END)
        self.comboGenero.set("")
        self.comboEspecie.set("")
        self.comboProprietario.set("")

    def buscarAnimal(self):
        animal = Animais()
        animal.id = self.txtidanimal.get()
        self.lblmsg["text"] = animal.selecionarAnimal()
        self.txtidanimal.delete(0, END)
        self.txtidanimal.insert(INSERT, animal.id)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, animal.nome)
        self.txtraca.delete(0, END)
        self.txtraca.insert(INSERT, animal.raca)
        self.comboGenero.set(animal.genero_descricao)
        self.comboEspecie.set(animal.especie_descricao)
        self.comboProprietario.set(animal.cliente_nome)
        if animal.genero_descricao!="":
            self.buscarEspecie("B")



