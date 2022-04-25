import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='datalake', user='root', password='Insira a senha para a conexão com o banco')

    criar_tabela_sql = '''create table tbl_produtos(
                            IdProduto int(11) not null,
                            NomeProduto varchar(70) not null,
                            Preco float not null,
                            Quantidade tinyint not null,
                            primary key (IdProduto))'''

    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print('Tabela de Produtos criada com sucesso!')

except mysql.connector.Error as erro:
    print(f'Falha ao criar tabela no MySQL {erro}')

finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada.')
print('\nPróxima aula: Inserção de Registros na tabela criada.')
