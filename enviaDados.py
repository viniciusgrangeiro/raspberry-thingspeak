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
          "+++++++++++++++++++++++++++++++++")

def insertComando(comando) : # Funcao que insere os comandos do usuario no banco de dados
    conn = sqlite3.connect('etec.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO eventos(evento, descricao) VALUES('comando', ?)""", comando)

def insertErro() : # Funcao que insere erros no banco de dados
    conn = sqlite3.connect('etec.db')
    cur = conn.cursor()
    cur.execute("""INSERT INTO eventos(evento, descricao) VALUES('falha', 'URL Inválida')""")

def contaTotalDeFalhas() : # Funcao que conta o total de registros cujo o evento seja falha
    conn = sqlite3.connect('etec.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM eventos WHERE evento = 'falha'")
    totalFalhas = cur.fetchall()
    return totalFalhas

imprimeMenu()
opcao = input('Insira o comando: ')

while 1:
    umidade = random.randint(1, 100)  # Variavel umidade randomica
    temperatura = random.randint(1, 50)  # Variavel temperatura randomica

    if opcao == '0': # Não enviar dados
        insertComando(opcao) # Insere a opcao de comando no banco
        print('Os dados não serão enviados.')
        break

    elif opcao == '1': # Envia temperatura
        try:
            time.sleep(5)
            payload = {'field1': temperatura}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
            insertComando(opcao) # Insere a opcao de comando no banco
            print('Temperatura:', temperatura)
            time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(e)
            insertErro() # Insere o registro de falha no banco

    elif opcao == '2': # Envia umidade
        try:
            payload = {'field2': umidade}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
            insertComando(opcao) # Insere a opcao de comando no banco
            print('Umidade:', umidade)
            time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(e)
            insertErro() # Insere o registro de falha no banco

    elif opcao == '3': # Envia temperatura e umidade
        try:
            payload = {'field1': temperatura, 'field2': umidade}
            requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)
            insertComando(opcao) # Insere a opcao de comando no banco
            print('Temperatura:', temperatura)
            print('Umidade....:', umidade)
            time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(e)
            insertErro() # Insere o registro de falha no banco
    else: # O usuario digitou um valor invalido
        print("Comando Inválido!")
        imprimeMenu()
        opcao = input('Insira o comando: ')
