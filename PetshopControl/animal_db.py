#para usar SQlite  utilize o Banco de banco
#from bancoprovisorio import Petshop

#para usar MySQL  utilize o Banco de bancomysql
from banco import Petshop

class Animais(object):
    def __init__(self, id = 0, nome = "", raca="", especie_id = 0,cliente_id = 0,cliente_nome = "",genero_descricao="",especie_descricao=""):
      self.info = {}
      self.id = id
      self.nome = nome
      self.raca = raca
      self.especie_id = especie_id
      self.cliente_id = cliente_id
      self.cliente_nome = cliente_nome
      self.genero_descricao = genero_descricao
      self.especie_descricao = especie_descricao

    def inserirAnimal(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("insert into animal (nome, raca, especie_id, cliente_id) values ('" + self.nome + "','" +
                    self.raca + "'," + str(self.especie_id) + ", " + str(self.cliente_id) + ")")
          banco.conexao.commit()
          c.close()
          return "Animal cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do animal!"

    def alterarAnimal(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("update animal set nome = '" + self.nome +"',raca = '" + str(self.raca) + "',especie_id = " + str(self.especie_id) + ",cliente_id = " + str(self.cliente_id) + " where id = "+ str(self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Animal atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do animal!"

    def excluirAnimal(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("delete from animal where id = " + str(self.id) + " ")
          banco.conexao.commit()
          c.close()
          return "Animal excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do animal"

    def selecionarAnimal(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select a.id,a.nome,a.raca, a.especie_id, g.descricao, e.descricao, a.cliente_id, c.nome "
                    "from animal a "
                    "left join especie e on (e.id=a.especie_id) "
                    "left join genero g on (g.id=e.genero_id) "
                    "left join cliente c on (a.cliente_id=c.id) "
                    "where a.id=" + str(self.id) + " ")

          for linha in c:
              self.id = linha[0]
              self.nome = linha[1]
              self.raca = linha[2]
              self.especie_id = linha[3]
              self.genero_descricao = linha[4]
              self.especie_descricao = linha[5]
              self.cliente_id = linha[6]
              self.cliente_nome = linha[7]
          c.close()
          return "Busca feita com sucesso!"

      except:
          return "Ocorreu um erro na busca do animal"

    def retornaAnimal(self):
        banco = Petshop()
        try:
            c = banco.conexao.cursor()
            c.execute("select id, nome from animal order by nome")
            rows = c.fetchall()
            c.close()
            return rows
        except:
            print("ERRO NA BUSCA DE ANIMAL")