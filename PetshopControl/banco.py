import pymysql

class Petshop():
     def __init__(self):
         self.conexao = pymysql.Connect('localhost','root','')
         self.conexao.select_db('petshop')

