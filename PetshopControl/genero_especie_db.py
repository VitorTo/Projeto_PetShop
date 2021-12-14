
from banco import Petshop
from collections import namedtuple

class GenerosEspecies(object):
    def __init__(self, genero_id = 0, genero_descricao = "",especie_id=0, especie_descricao=""):
      self.info = {}
      self.genero_id = genero_id
      self.genero_descricao = genero_descricao
      self.especie_id = especie_id
      self.especie_descricao = especie_descricao

    def retornarEspecies(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select id,descricao from especie where genero_id = " + str(self.genero_id) + " ")
          rows = c.fetchall()
          c.close()
          return rows
      except:
          print("ERRO DE CONEXÃO")

    def retornarGeneros(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select id,descricao from genero order by descricao")
          rows = c.fetchall()
          c.close()
          return rows
      except:
          print("ERRO DE CONEXÃO")

    def retornarGenerosEspecies(self):
      banco = Petshop()
      try:
          c = banco.conexao.cursor()
          c.execute("select b.descricao,a.descricao from especie a inner join genero b on a.genero_id=b.id order by 1,2")
          rows = c.fetchall()
          c.close()
          return rows
      except:
          print("ERRO DE CONEXÃO")