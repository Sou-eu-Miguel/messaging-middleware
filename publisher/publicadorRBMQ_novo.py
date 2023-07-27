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
port = int(config.get("RABBITMQ","port"))
usuario = config.get("RABBITMQ","usuario")
senha = config.get("RABBITMQ","senha")
vexchange = config.get("RABBITMQ","vexchange")
vhost = config.get("RABBITMQ","vhost")

#print(f"Parâmetros lidos: {host}:{port}, user:{usuario}, virtual_host:{vhost} e exchange:{vexchange}\n")

# connectar no servidor
#credenciais = pika.PlainCredentials (username=usuario,password=senha)
#conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port,virtual_host=vhost, credentials=credenciais))

#conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port,virtual_host=vhost,credentials=credenciais,heartbeat=30))

def conectarRBMQ(host,port,user,passwd,vhost):
    credenciais = pika.PlainCredentials(user,passwd)
    conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port,virtual_host=vhost,credentials=credenciais))
    return(conexao)


def pubMensRBMQ(mensagem,pExchange):
    #exchange=vexchange
    routk="*"
    channel.basic_publish(exchange=pExchange,routing_key=routk,body=mensagem)
    #channel.basic_publish(exchange=exchange,body=mensagem)


def desconectarRBMQ():    
    conexao.close()
    #cnx.close()


def montaPayload (pContext, pMsg):
    return (json.dumps({"context":pContext,"body":pMsg}).encode("utf-8"))


# connectar no servidor
credenciais = pika.PlainCredentials (username=usuario,password=senha)
conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host,virtual_host=vhost, credentials=credenciais))

#print(conexao)
#conexao = conectarRBMQ('localhost',15672,'guest','guest','middleware')    

#cnx = conectarRBMQ(host,int(port),usuario,senha,vhost)    
#print(cnx)
channel = conexao.channel()
#channel = cnx.channel()

#vmensagem = json.dumps({
#        "context": "vasco", 
#        "body": "Ta indo para segunda..."
#            }).encode("utf-8")


print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Digite a mensagem a ser enviada: ")

# monta e apresenta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()


pubMensRBMQ(mensagem=payload,pExchange=vexchange)
print("Mensagem enviada para a fila do RabbitMQ!!")
desconectarRBMQ()
