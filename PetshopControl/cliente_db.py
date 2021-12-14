
from banco import Petshop

class Clientes(object):
    def __init__(self, id = 0, nome = "", email = "", telefone = "", endereco = "", cpf = ""):
      self.info = {}
      self.id = id
      self.nome = nome
      self.email = email
      self.telefone = telefone
      self.endereco = endereco
      self.cpf = cpf

    def inserirCliente(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("insert into cliente (nome, email, telefone, endereco, cpf) "
                    "values ('" + self.nome + "', '" +self.email + "', '" + self.telefone + "', '" +
                    self.endereco + "', '" + self.cpf + "' )")
          banco.conexao.commit()
          c.close()
          return "Cliente cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do cliente!"

    def alterarCliente(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("update cliente set nome = '" + self.nome + "',email = '" + self.email + "', telefone = '"
                    + self.telefone +"', endereco = '" + self.endereco + "', cpf = '" + self.cpf +"' where id = "
                    +str( self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Cliente atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do cliente!"

    def excluirCliente(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("delete from cliente where id = " +str( self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Cliente excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do cliente"

    def selecionarUsuario(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select * from cliente where id = " + self.id + "  ")
          for linha in c:
              self.id = linha[0]
              self.nome = linha[1]
              self.email = linha[2]
              self.telefone = linha[3]
              self.endereco = linha[4]
              self.cpf = linha[5]
          c.close()
          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do cliente"

    def retornaCliente(self):
        banco = Petshop()
        try:
            c = banco.conexao.cursor()
            c.execute("select id, nome from cliente order by nome")
            rows = c.fetchall()
            c.close()
            return rows
        except:
            print("ERRO NA BUSCA DE CLIENTE")