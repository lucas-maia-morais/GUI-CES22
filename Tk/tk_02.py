from contextlib import redirect_stderr
from tkinter import *

class Form:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.btnmsg = Button(frame, text="Mensagem", command=self.mostra_mensagem)
        self.btnmsg.pack(side=LEFT)
        self.btnsair = Button(frame, text="Sair", fg="red", command=frame.quit)
        self.btnsair.pack(side=RIGHT)

    
    def mostra_mensagem(self):
        print("Olá")

root = Tk()
app = Form(root)
root.mainloop()