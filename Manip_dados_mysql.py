import mysql.connector
from mysql.connector import Error


class Manip_dados_mysql:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def conectar_mysql(self):
        con = mysql.connector.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )
        return con

    def comando_insert_produtos(self, id_prod, nome_prod,preco_prod, quant_prod):
        dados = str(id_prod) + ",'" + str(nome_prod) + "'," + str(preco_prod) + "," + str(quant_prod) + ")"
        declaracao = '''insert into tbl_produtos
        (IdProduto, NomeProduto, Preco, Quantidade)
        values('''
        sql = declaracao + dados
        return sql

    def exec_sql(self, sql):
        con = self.conectar_mysql()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()
        


insercao = Manip_dados_mysql("localhost", "datalake", "root", "insira aqui sua senha para conexão com o banco de dados")
comando_insert = insercao.comando_insert_produtos(1, 'Calculadora', 5.98, 2)
insercao.exec_sql(comando_insert)