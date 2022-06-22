from Banco import Banco


class Participante(object):


    def __init__(self, id=0, nome="", login="", senha="", email="", endereco="", telefone=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    
    def insertParticipante(self):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()

            c.execute("insert into participante (nome, login, senha, email, endereco, telefone) values ('" + self.nome + "', '" +
                      self.login + "', '" + self.senha + "', '" + self.email + "', '" + self.endereco + "', '" + self.telefone + "' )")

            banco.conexao.commit()
            c.close()

            return "Participante cadastrado com sucesso"
        except:
            return "Ocorreu um erro na inserção do participante"


    @property
    def updateParticipante(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update participante set nome = '" + self.nome + "', login = '" + self.login +
                        "',  senha = '" + self.senha +
                        "',  email = '" + self.email +
                        "',  endereco = '" + self.endereco +
                        "',  telefone = '" + self.telefone + "' where id = " + self.id + " ")

            banco.conexao.commit()
            c.close()

            return "participante atualizado com sucesso"
        except:
            return "Ocorreu um erro na alteração do participante"

    
    @property
    def deleteParticipante(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from participantes where id = " + self.id + " ")

            banco.conexao.commit()
            c.close()

            return "Participante excluido com sucesso"
        except:
            return "Ocorreu um erro na exclusão do participante"

    
    def select_participante(self, id):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from participantes where id = " + id + " ")

            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.login = linha[2]
                self.senha = linha[3]
                self.email = linha[4]
                self.endereco = linha[5]
                self.telefone = linha[6]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do participante"

            