import mysql.connector
from mysql.connector import Error

print('Rotina para cadastro de produtos no banco de dados.')
print('Entre com os dados como solicitado.')


lanca_valores = True
while lanca_valores:
    # Lançamento do id do produto
    valida = False
    while not valida:
        idProd = input('Id do produto: ')
        if idProd == '':
            print('É preciso informar um ID para o produto.')
        else:
            try:
                idProd = int(idProd)
                if idProd <= 0:
                    print('ID inválido.')
                else:
                    valida = True
            except:
                print('ID Inválido.')

    # Lançamento do nome do produto
    valida = False
    while not valida:
        nomeProd = input('Nome do produto: ')
        if nomeProd == '':
            print('É preciso informar um nome para o produto.')
        else:
            nomeProd = str(nomeProd).strip().title()
            valida = True

    # Lançamento do preço do produto
    valida = False
    while not valida:
        precoProd = input('Preço do produto: ')
        if precoProd == '':
            print('É preciso informar um preço para o produto.')
        else:
            try:
                precoProd = float(precoProd)
                if precoProd <= 0:
                    print('O preço do produto deve ser maior que zero.')
                else:
                    valida = True
            except:
                print('Preço inválido.')
        
    # Lançamento da quantidade do produto
    valida = False
    while not valida:
        quantProd = input('Quantidade do produto: ')
        if quantProd == '':
            print('É preciso informar uma quantidade para o produto')
        else:
            try:
                quantProd = int(quantProd)
                if quantProd <= 0:
                    print('A quantidade do produto deve ser maior que zero.')
                else:
                    valida = True
            except:
                print('Quantidade inválida.')

    # Cria a string de insert into para lançar os dados no banco de dados
    dados = str(idProd) + ",'" + str(nomeProd) + "'," + str(precoProd) + "," + str(quantProd) + ')'
    declaracao = '''insert into tbl_produtos
    (IdProduto, NomeProduto, Preco, Quantidade)
    values('''
    sql = declaracao + dados
    
    # Realiza a conexão com o banco de dados para realizar o lançamento dos dados informados
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'wel_informatica', user =  'root', password = 'Insira a senha para a conexão com o banco')
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(cursor.rowcount, 'registros foram inserids na tabela!')
        cursor.close()

    except Error as erro:
        print(f'Falha ao inserir dados no MYSQL {erro}')

    finally:
        # Questiona se gostaria de relizar mais um lançamento
        valida = False
        while not valida:
            continua = input('Gostaria de inserir mais dados?(s/n): ').strip().lower()
            if continua == '':
                print('Por favor, digite (s/n) para informar se deseja continuar.')
            else:
                if continua == 's':
                    valida = True
                elif continua == 'n':
                    valida = True
                    lanca_valores = False
                    if(con.is_connected()):
                        cursor.close()
                        con.close()
                        print('Conexão ao MYSQL finalizada.')
                else:
                    print('Por favor, digite (s/n) para informar se deseja continuar.')
    
    