from tkinter import *
from PIL import Image, ImageTk
#import tkinter as tk
#from easygui.boxes.fileopen_box import tk


class Geral:
    def __init__(self, master=None):
        self.container1 = Frame(master,bg="grey61")
        self.container1.pack()
        img = ImageTk.PhotoImage(Image.open("image/PetshopIMAGE.PNG"))
        imagem = Label(self.container1, image=img,bg="grey61")
        imagem.image=img
        imagem.pack()

        self.informacoes = Label(self.container1, text="",bg="grey61")
        self.informacoes.pack()




"""
class Geral:
    def __init__(self, master=None):
        self.nossaTela = master

        img = Image.open("PETSHOP.PNG")
        self.minhaImagem = ImageTk.PhotoImage(img)
        self.lbl = tk.Label(self.nossaTela,image = self.minhaImagem)
        self.lbl.image = self.minhaImagem
        self.lbl.pack()
"""

