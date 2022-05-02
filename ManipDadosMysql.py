import mysql.connector
from mysql.connector import Error


class ManipDadosMysql:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def conectar_mysql(self):
        try:
            con = mysql.connector.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password
            )
            return con
        except:
            print(f'Não foi possível se conectar à base {self.database}. Verifique a conexão.')
            return None


    def copia_dados(self, tabela):        
        try:
            con = self.conectar_mysql()
            sql_select = f"select * from {tabela}"
            cursor = con.cursor()
            cursor.execute(sql_select)
            dados_origem = cursor.fetchall()
            cursor.close()
            con.close()
            return dados_origem
        except:
            return None
            
        
    def cola_dados(self, tabela, dados_origem):
        try:
            con = self.conectar_mysql()
            sql_insert = f"insert into {tabela} values (%s, %s, %s, %s)"
            cursor = con.cursor()
            for dado in dados_origem:
                try:
                    cursor.execute(sql_insert, dado)
                    print(f'Registro dom id {dado[0]} inserido com sucesso.')
                except:
                    print(f'Registro com id {dado[0]} não foi inserido pois já está na tabela.')
            cursor.close()
            con.commit()
            con.close()
        except:
            return None
        
        
# Criação das instâncias de conexão e execução da função de inserção de dados
con_dl = ManipDadosMysql('localhost', 'datalake', 'usuario', 'senha')
con_dw = ManipDadosMysql('localhost', 'data_warehouse', 'usuario', 'senha')

dados_origem = con_dl.copia_dados('tbl_produtos')
con_dw.cola_dados('tbl_produtos', dados_origem)

