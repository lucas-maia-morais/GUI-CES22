from contextlib import redirect_stderr
from tkinter import *

class Form:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.lblmsg = Label(frame, text="Bem-vindo(a)!")
        self.lblmsg.pack(side=TOP)
        self.btnmsg = Button(frame, text="Mensagem", command=self.mostra_mensagem)
        self.btnmsg.pack(side=LEFT)
        self.btnsair = Button(frame, text="Sair", fg="red", command=frame.quit)
        self.btnsair.pack(side=RIGHT)

    
    def mostra_mensagem(self):
        if self.lblmsg["text"] == "Bem-vindo(a)!":
            self.lblmsg["text"]="Olá :"
        else:
            self.lblmsg["text"]="Bem-vindo(a)!"

root = Tk()
app = Form(root)
root.mainloop()