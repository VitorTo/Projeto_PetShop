
from banco import Petshop

class Atendimento(object):
    def __init__(self, id = 0, servico = "", valor = "", cliente_nome = "",cliente_id = 0 , animal_id = 0, animal_nome = "" ):
      self.info = {}
      self.id = id
      self.servico = servico
      self.cliente_nome = cliente_nome
      self.cliente_id = cliente_id
      self.animal_nome = animal_nome
      self.animal_id = animal_id
      self.valor = valor

    def selecionaAtendimento(self):
        banco = Petshop()
        try:
            c = banco.conexao.cursor()
            c.execute("select a.id,a.servico,c.nome,an.nome,a.valor from atendimento a left join cliente c on (c.id=a.cliente_id) left join animal an on (an.id=a.animal_id) where a.id=" + str(self.id) + "  ")
            for linha in c:
                self.id = linha[0]
                self.servico = linha[1]
                self.cliente_nome = linha[2]
                self.animal_nome = linha[3]
                self.valor = linha[4]

            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca "


    def alterarAtendimento(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("update atendimento set cliente_id = " + str(self.cliente_id) + ", animal_id = " + str(
              self.animal_id) + ", servico = '" + self.servico + "', valor = '" + self.valor + "' where id = " + str(
              self.id) + " ")
         # c.execute("update atendimento set servico = '" + self.servico + "',cliente_id = " + str(self.cliente_id) + ", animal_id = " +str(self.animal_id) + ", valor = '" + self.valor + "'  where id = " + str(self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Atendimento atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do Atendimento!"

    def excluirAtendimento(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("delete from cliente where id = " + str(self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Atendimento excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do Atendimento"


    def mostrarCliente(self):
        banco = Petshop()
        try:
            c = banco.conexao.cursor()
            c.execute("select id, nome from cliente order by nome")
            rows = c.fetchall()
            c.close()
            return rows
        except:
            print("ERRO NA BUSCA DE CLIENTE")

    def retornarValor(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select c.nome,servico,valor,a.id from atendimento a , cliente c order by c.id")
          rows = c.fetchall()
          c.close()
          return rows
      except:
          print("ERRO DE CONEXÃO")


    def retornarNome(self):
        banco = Petshop()
        try:
            c = banco.conexao.cursor()
            c.execute("select c.nome,a.id from atendimento a , cliente c where a.id = c.id")
            rows = c.fetchall()
            c.close()
            return rows
        except:
            print("ERRO DE CONEXÃO")


    # Pensei em colocar inserir pra fazer possiveis alterações sem precisar abrir o banco
    def inserirAtendimento(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("insert into atendimento (cliente_id, animal_id, servico, valor) values ("+str(self.cliente_id)+","+str(self.animal_id)+",'"+self.servico+"',"+self.valor+")")
          banco.conexao.commit()
          c.close()
          return "Atendimento cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do atendimento!"



