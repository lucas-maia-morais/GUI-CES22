from cProfile import label
from Participantes import Musica
from tkinter import *

class SisMus:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")


        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 18
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="* Minhas musicas *")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblcd_musica = Label(self.container2, text="Código Música", font=self.fonte, width=15)
        self.lblcd_musica.pack(side=LEFT)

        self.txtcd_musica = Entry(self.container2)
        self.txtcd_musica["width"] = 10
        self.txtcd_musica["font"] = self.fonte
        self.txtcd_musica.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMusica
        self.btnBuscar.pack(side=RIGHT)

        self.lbltitulo = Label(self.container3, text="Titulo:", font=self.fonte, width=10)
        self.lbltitulo.pack(side=LEFT)

        self.txttitulo = Entry(self.container3)
        self.txttitulo["width"] = 25
        self.txttitulo["font"] = self.fonte
        self.txttitulo.pack(side=LEFT)

        self.lblartista = Label(self.container4, text="Artista:", font=self.fonte, width=18)
        self.lblartista.pack(side=LEFT)

        self.txtartista = Entry(self.container4)
        self.txtartista["width"] = 25
        self.txtartista["font"] = self.fonte
        self.txtartista.pack(side=LEFT)

        self.lblgenero = Label(self.container5, text="Gênero:", font=self.fonte, width=18)
        self.lblgenero.pack(side=LEFT)

        self.txtgenero = Entry(self.container5)
        self.txtgenero["width"] = 25
        self.txtgenero["font"] = self.fonte
        self.txtgenero.pack(side=LEFT)

        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirMusica
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarMusica
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirMusica
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", 9, "italic")
        self.lblmsg.pack()

    def inserirMusica(self):
        music = Musica()

        music.titulo = self.txttitulo.get()
        music.artista = self.txtartista.get()
        music.genero = self.txtgenero.get()

        self.lblmsg["text"] = music.insertMusic()

        self.txtcd_musica.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtartista.delete(0, END)
        self.txtgenero.delete(0, END)

    def alterarMusica(self):
        music = Musica()

        music.cd_musica = self.txtcd_musica.get()
        music.titulo = self.txttitulo.get()
        music.artista = self.txtartista.get()
        music.genero = self.txtgenero.get()

        self.lblmsg["text"] = music.updateMusic

        self.txtcd_musica.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtartista.delete(0, END)
        self.txtgenero.delete(0, END)

    def excluirMusica(self):
        music = Musica()

        music.titulo = self.txttitulo.get()
        music.titulo = self.txttitulo.get()
        music.artista = self.txtartista.get()
        music.genero = self.txtgenero.get()

        self.lblmsg["text"] = music.updateMusic

        self.txtcd_musica.delete(0, END)
        self.txttitulo.delete(0, END)
        self.txtartista.delete(0, END)
        self.txtgenero.delete(0, END)

    def buscarMusica(self):
        music = Musica()

        cd_musica = self.txtcd_musica.get()

        self.lblmsg["text"] = music.selectMusic(cd_musica)
        
        self.txtcd_musica.delete(0, END)
        self.txtcd_musica.insert(INSERT, music.cd_musica)

        self.txttitulo.delete(0, END)
        self.txtcd_musica.insert(INSERT, music.titulo)

        self.txtartista.delete(0, END)
        self.txtartista.insert(INSERT, music.artista)

        self.txtgenero.delete(0, END)
        self.txtgenero.insert(INSERT, music.genero)


root = Tk()
SisMus(root)
root.mainloop()