from cliente_db import Clientes
from tkinter import *



class IFClientes:
    def __init__(self, master=None):
        self.fonte = ("Palatino Linotype", "14")
        self.container1 = Frame(master,bg="grey61")
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master,bg="grey61")
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master,bg="grey61")
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master,bg="grey61")
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master,bg="grey61")
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master,bg="grey61")
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master,bg="grey61")
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master,bg="grey61")
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master,bg="grey61")
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :",width= 40, bg="grey61", fg="#92E3A9")
        self.titulo["font"] = ("Palatino Linotype", "28", "bold")
        self.titulo.pack ()

        self.lblid = Label(self.container2, text="idCliente:", font=self.fonte,bg='#92E3A9',fg="grey11", width=10)
        self.lblid.pack(side=LEFT)

        self.txtid = Entry(self.container2)
        self.txtid["width"] = 10
        self.txtid["font"] = self.fonte
        self.txtid.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10,bg="grey11", fg="White")
        self.btnBuscar["command"] = self.buscarCliente
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblemail= Label(self.container4, text="E-mail:",
        font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container4)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbltelefone = Label(self.container5, text="Telefone:",
        font=self.fonte, width=10, bg="grey61", fg="white")
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container5)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)


        self.lblendereco= Label(self.container6, text="Endereço:",
        font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblendereco.pack(side=LEFT)

        self.txtendereco = Entry(self.container6)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lblcpf= Label(self.container7, text="CPF:",font=self.fonte, width=10, bg="grey61", fg="white")
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container7)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntInsert["command"] = self.inserirCliente
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntAlterar["command"] = self.alterarCliente
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte, width=12, bg="grey11", fg="white")
        self.bntExcluir["command"] = self.excluirCliente
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", bg="grey61",fg="White")
        self.lblmsg["font"] = ("Palatino Linotype", "24", "italic")
        self.lblmsg.pack()


    def inserirCliente(self):
        cliente = Clientes()
        cliente.nome = self.txtnome.get()
        cliente.email = self.txtemail.get()
        cliente.telefone = self.txttelefone.get()
        cliente.endereco = self.txtendereco.get()
        cliente.cpf = self.txtcpf.get()
        self.lblmsg["text"] = cliente.inserirCliente()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtcpf.delete(0, END)

    def alterarCliente(self):
        cliente = Clientes()
        cliente.id = self.txtid.get()
        cliente.nome = self.txtnome.get()
        cliente.email = self.txtemail.get()
        cliente.telefone = self.txttelefone.get()
        cliente.endereco = self.txtendereco.get()
        cliente.cpf = self.txtcpf.get()

        self.lblmsg["text"] = cliente.alterarCliente()

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtcpf.delete(0, END)

    def excluirCliente(self):
        cliente = Clientes()
        cliente.id = self.txtid.get()
        self.lblmsg["text"] = cliente.excluirCliente()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtcpf.delete(0, END)

    def buscarCliente(self):
        cliente = Clientes()
        cliente.id = self.txtid.get()
        self.lblmsg["text"] = cliente.selecionarUsuario()
        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, cliente.id)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, cliente.nome)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, cliente.email)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,cliente.telefone)
        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT, cliente.endereco)
        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT,cliente.cpf)
