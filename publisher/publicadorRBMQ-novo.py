import json
import pika
import configparser

'''
host="localhost"
port=15672
user="guest"
passwd="guest"
vhost="middleware" 
vexchange="generic"
'''
#importar as configurações de acesso
config = configparser.ConfigParser(delimiters="=")
config.read("publisher-config.ini")
host = config.get("RABBITMQ","host")
port = config.get("RABBITMQ","port")
usuario = config.get("RABBITMQ","usuario")
senha = config.get("RABBITMQ","senha")
vexchange = config.get("RABBITMQ","vexchange")
vhost = config.get("RABBITMQ","vhost")


def conectarRBMQ(host,port,user,passwd,vhost):
    credenciais = pika.PlainCredentials(user,passwd)
    #conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port, virtual_host=vhost, credentials=credenciais))
    conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port,virtual_host=vhost,credentials=credenciais))
    #return(conexao)


#print("conectado...")
#print()
#channel = conexao.channel()
#channel.queue_declare(queue='generic',durable=False)

def pubMensRBMQ(mensagem,pExchange):
    #exchange=vexchange
    routk="*"
    channel.basic_publish(exchange=pExchange,routing_key=routk,body=mensagem)
    #channel.basic_publish(exchange=exchange,body=mensagem)

def desconectarRBMQ():    
    conexao.close()

vmensagem = json.dumps({
        "context": "vasco", 
        "body": "Ta indo para segunda..."
            }).encode("utf-8")

#credenciais = pika.PlainCredentials(usuario,senha)
#conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=int(port),virtual_host=vhost, credentials=credenciais))

#conexao = conectarRBMQ('localhost',15672,'guest','guest','middleware')    
conexao = conectarRBMQ(host,int(port),usuario,senha,vhost)    
channel = conexao.channel()


pubMensRBMQ(mensagem=vmensagem,pExchange=vexchange)
print("Mensagem enviada!!")
desconectarRBMQ()
