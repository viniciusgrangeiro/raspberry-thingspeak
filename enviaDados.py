import time
import requests
import random

while 1:
    umidade = random.randint(1, 100)  # Variavel com a umidade randomica
    temperatura = random.randint(1, 50) # Variavel com a temperatura randomica
    try: # Tenta enviar os dados de temperatura para a API
        x = requests.get("https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&field1=" + str(temperatura))
        print('Temperatura: {:.2f}'.format(temperatura))
        time.sleep(5)
        payload = {'field1': temperatura}
    except requests.exceptions.HTTPError: # Exibe o erro de requisição HTTP caso haja um erro
        print('Falha ao enviar dados...')
        print(x.status_code)
    try:
        x = requests.get("https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&field2=" + str(umidade))
        print('Umidade: {:.2f}'.format(umidade))
        time.sleep(5)
        payload = {'field2': umidade}
    except requests.exceptions.HTTPError:
        print('Falha ao enviar dados...')
        print(x.status_code)



# x = requests.get("https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&field1=" + str(temperatura))
# print('Temperatura: {:.2f}'.format(temperatura))
# x = requests.get("https://api.thingspeak.com/update?api_key=HV0JXNMY9KVX23SH&field2=" + str(umidade))
# print('Umidade....: {:.2f}'.format(umidade))

# time.sleep(1)
# payload = {'field1': temperatura, 'field2': umidade}
# if x.status_code == 200:
#     print('Dados enviados com sucesso')
# else:
#     print('Falha ao enviar dados...')
# print(x.status_code)
#
# print(temperatura)
# print(umidade)