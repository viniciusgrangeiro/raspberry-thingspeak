import time
import requests
import random
import sqlite3

def imprimeMenu() :
    print("++++++++++++++++++++++++++++++++ \n"
          "Escolha o comando \n"
          "+++++++++++++++++++++++++++++++++ \n"
          "0 - Não envia dados \n"
          "1 - Enviar temperatura \n"
          "2 - Enviar umidade \n"
          "3 - Enviar temperatura e umidade \n"
          "+++++++++++++++++++++++++++++++++ \n")

def insertComando(valor) :
    conn = sqlite3.connect('thingspeak.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO eventos(evento, descricao) VALUES('comando', ?)""", valor)

def insertErro(erro) :
    conn = sqlite3.connect('thingspeak.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO eventos(evento, descricao) VALUES('falha', ?)""", erro)

imprimeMenu()

opcao = int(input('Insira o comando: '))

while 1:
    umidade = random.randint(1, 100)  # Variavel com a umidade randomica
    temperatura = random.randint(1, 50)  # Variavel com a temperatura randomica

    if opcao == 0:
        insertComando(opcao)
        print('Não enviar dados...')

    elif opcao == 1:
        try:
            # Envia temperatura
            payload = {'field1': temperatura}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
        except requests.exceptions.RequestException as e:
            insertErro(e)

        print('Temperatura:', temperatura)
    elif opcao == 2:
        try:
            # Envia umidade
            payload = {'field2': umidade}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
        except requests.exceptions.RequestException as e:
            insertErro(e)

        print('Umidade:', umidade)
    elif opcao == 3:
        try:
            # Envia temperatura e umidade
            payload = {'field1': temperatura, 'field2': umidade}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
        except requests.exceptions.RequestException as e:
            insertErro(e)

        print('Temperatura:', temperatura)
        print('Umidade....:', umidade)
    else:
        # não faz nada
        print("Comando Inválido!")

    time.sleep(5)
    # try:
    #     # Envia os dados para a API
    #     payload = {'field1': temperatura, 'field2': umidade}
    #     requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
    #
    #     # Imprime no console a temperatura e umidade atual
    #     print('Temperatura: {:.2f}'.format(temperatura))
    #     print('Umidade....: {:.2f}'.format(umidade))
    #     print('Dados enviados com sucesso')
    # except requests.exceptions.RequestException as e:  # Exibe a excecao
    #     # Imprime o erro
    #     print(e)
    #
    #     print('Inserindo erros no banco de dados...')
    #     sqliteConn = sqlite3.connect('thingspeak.db')
    #     cur = sqliteConn.cursor()
    #     cur.execute("INSERT INTO erros(desc_erro) VALUES('URL Inválida')")
    #     sqliteConn.commit()
    #     print('Dados inseridos com sucesso!')
    #
    #
    # # Pausa a execucao por 5 segundos
    # time.sleep(5)
