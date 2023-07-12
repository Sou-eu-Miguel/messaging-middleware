#import classeRabbit as rbmq
import json 

# replica o caracter a quantdade de vezes desejada
def repl(c, n):
    ret = ""
    for x in range(n):
        ret += c
    return (ret)

# monta o menu de e retorna a opção escolhida para envio da mensagem
def sendTo():
    #clear
    vMenu = [-1,1,2,3]
    print (repl("=",40))
    print ("| 1 - Enviar mensagem para RabbitMq    |")
    print ("| 2 - Enviar mensagem para Kafka       |")
    print ("| 3 - Enviar mensagem para MQTT        |")
    print (repl("-",40))
    print ("Escolha o número dentre as opções acima ou -1 para sair")
    try:
        vOpt = int(input(""))
        while vOpt not in vMenu:
            print ("Escolha o número dentre as opções acima ou -1 para sair.")
            vOpt = int(input(""))
        return (vOpt)
    except:
        return(-1)
    
def montaPayload (pContext, pMsg):
    return ({
        "contexto": pContext, 
        "mensagem": pMsg
            })    

# Obtem o contexto e mensagem para montagem do payload
vContext = input("Informe o contexto da mensagem: ")
vMsg = input("Informe a mensagem a ser enviada: ")

payload = montaPayload(vContext,vMsg)
print()
print (payload)
print()

#!/usr/bin/env python
import pika

host='192.168.0.25'
port='15672'
user='guest'
passwd='guest'

credenciais = pika.PlainCredentials(user,passwd)

conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credenciais))

channel = conexao.channel()

channel.queue_declare(queue='geral')

channel.basic_publish(exchange='distrib',
                      routing_key='geral',
                      body='Hello World!')

print(" [x] enviei 'Hello World!'")
conexao.close()




