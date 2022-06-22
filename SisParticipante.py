from cProfile import label
from Participantes import Participante
from tkinter import *

class SisParticipant:
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
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 18
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["padx"] = 15
        self.container12.pack()

        self.titulo = Label(self.container1, text="* Participantes *")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblid = Label(self.container2, text="Id participante", font=self.fonte, width=15)
        self.lblid.pack(side=LEFT)

        self.txtid = Entry(self.container2)
        self.txtid["width"] = 10
        self.txtid["font"] = self.fonte
        self.txtid.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarParticipante
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbllogin = Label(self.container4, text="Login:", font=self.fonte, width=18)
        self.lbllogin.pack(side=LEFT)

        self.txtlogin = Entry(self.container4)
        self.txtlogin["width"] = 25
        self.txtlogin["font"] = self.fonte
        self.txtlogin.pack(side=LEFT)

        self.lblsenha = Label(self.container5, text="Senha:", font=self.fonte, width=18)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container5)
        self.txtsenha["width"] = 25
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.lblemail = Label(self.container6, text="Email:", font=self.fonte, width=18)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container6)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblender = Label(self.container7, text="Endereco:", font=self.fonte, width=18)
        self.lblender.pack(side=LEFT)

        self.txtender = Entry(self.container7)
        self.txtender["width"] = 25
        self.txtender["font"] = self.fonte
        self.txtender.pack(side=LEFT)

        self.lbltel = Label(self.container8, text="Telefone:", font=self.fonte, width=18)
        self.lbltel.pack(side=LEFT)

        self.txttel = Entry(self.container8)
        self.txttel["width"] = 25
        self.txttel["font"] = self.fonte
        self.txttel.pack(side=LEFT)

        self.btnInsert = Button(self.container11, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirParticipante
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container11, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarParticipante
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container11, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirParticipante
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container12, text="")
        self.lblmsg["font"] = ("Verdana", 9, "italic")
        self.lblmsg.pack()

    def inserirParticipante(self):
        participant = Participante()

        participant.nome = self.txtnome.get()
        participant.login = self.txtlogin.get()
        participant.senha = self.txtsenha.get()
        participant.email = self.txtemail.get()
        participant.endereco = self.txtender.get()
        participant.telefone = self.txttel.get()

        self.lblmsg["text"] = participant.insertParticipante()

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtlogin.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtender.delete(0, END)
        self.txttel.delete(0, END)

    def alterarParticipante(self):
        participant = Participante()

        participant.id = self.txtid.get()
        participant.nome = self.txtnome.get()
        participant.login = self.txtlogin.get()
        participant.senha = self.txtsenha.get()
        participant.email = self.txtemail.get()
        participant.endereco = self.txtender.get()
        participant.telefone = self.txttel.get()

        self.lblmsg["text"] = participant.updateParticipante

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtlogin.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtender.delete(0, END)
        self.txttel.delete(0, END)

    def excluirParticipante(self):
        participant = Participante()

        participant.id = self.txtid.get()
        participant.nome = self.txtnome.get()
        participant.login = self.txtlogin.get()
        participant.senha = self.txtsenha.get()
        participant.email = self.txtemail.get()
        participant.endereco = self.txtender.get()
        participant.telefone = self.txttel.get()

        self.lblmsg["text"] = participant.deleteParticipante

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtlogin.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtender.delete(0, END)
        self.txttel.delete(0, END)

    def buscarParticipante(self):
        participant = Participante()

        id = self.txtid.get()

        self.lblmsg["text"] = participant.select_participante(id)
        
        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, participant.id)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, participant.nome)

        self.txtlogin.delete(0, END)
        self.txtlogin.insert(INSERT, participant.login)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, participant.senha)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, participant.email)

        self.txtender.delete(0, END)
        self.txtender.insert(INSERT, participant.endereco)

        self.txttel.delete(0, END)
        self.txttel.insert(INSERT, participant.telefone)


root = Tk()
SisParticipant(root)
root.mainloop()