import json
import pika

host="localhost"
port=15672
user="guest"
passwd="guest"
vhost="middleware" 
vexchange="generic"

credenciais = pika.PlainCredentials(user,passwd)

conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host, virtual_host=vhost, credentials=credenciais))

#print("conectado...")
#print()
channel = conexao.channel()
#channel.queue_declare(queue='generic',durable=False)
def pubMensRBMQ(mensagem):
    exchange=vexchange
    routk="*"
    channel.basic_publish(exchange=exchange,routing_key=routk,body=mensagem)
    #channel.basic_publish(exchange=exchange,body=mensagem)


def desconectarRBMQ():    
    conexao.close()

vmensagem = json.dumps({
        "context": "vasco", 
        "body": "Ta indo para segunda..."
            })

pubMensRBMQ(mensagem=vmensagem)



