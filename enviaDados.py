import time
import requests
import random
import sqlite3

while 1:
    umidade = random.randint(1, 100)  # Variavel com a umidade randomica
    temperatura = random.randint(1, 50)  # Variavel com a temperatura randomica

    try:
        # Envia os dados para a API
        payload = {'field1': temperatura, 'field2': umidade}
        requests.get('https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&', params=payload)

        # Imprime no console a temperatura e umidade atual
        print('Temperatura: {:.2f}'.format(temperatura))
        print('Umidade....: {:.2f}'.format(umidade))
        print('Dados enviados com sucesso')
    except requests.exceptions.RequestException as e:  # Exibe a excecao
        # Imprime o erro
        print(e)

        print('Inserindo erros no banco de dados...')
        sqliteConn = sqlite3.connect('thingspeak.db')
        cur = sqliteConn.cursor()
        cur.execute("INSERT INTO erros(desc_erro) VALUES('URL Inválida')")
        sqliteConn.commit()
        print('Dados inseridos com sucesso!')


    # Pausa a execucao por 5 segundos
    time.sleep(5)
