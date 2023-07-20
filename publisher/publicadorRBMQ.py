import json
import pika

host="localhost"
port=15672
user="guest"
passwd="guest"
vhost="middleware" 

credenciais = pika.PlainCredentials(user,passwd)

conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host, virtual_host="middleware", credentials=credenciais))

#print("conectado...")
#print()
channel = conexao.channel()
#channel.queue_declare(queue='geral')
def pubMensRBMQ(mensagem):
    exchange=mensagem["contexto"]
    routk=mensagem["contexto"]
    channel.basic_publish(exchange=exchange,
                    routing_key=routk,
                    body=mensagem)

def desconectarRBMQ():    
    conexao.close()

