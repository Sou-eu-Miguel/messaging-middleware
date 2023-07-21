from kafka import KafkaProducer
import json

kfk=KafkaProducer()

def pubMensKFK(topico, mensagem):
    msg=json.dumps(mensagem).encode("utf-8")
    #print(json.loads(msg.decode('utf-8')))
    #kfk.send (topico, json.loads(msg.decode('utf-8')))
    kfk.send (topico, msg)
        

# Configurações de conexão
#servidorKFK = 'localhost:9092'
host='localhost'
port=9092
#bootstrap_servers = host:port

# Criando uma instância do gerenciador de filas Kafka
def conectarKFK (pServer):
    #kfk = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    kfk = KafkaProducer(bootstrap_servers=pServer)


#print(f"Conectado: {kafka.bootstrap_connected}")

# Fechando a conexão
def desconectarKFK():
    kfk.close()
       
# iniciando o kafka
conectarKFK(f"{host}:{port}")

# Criando um payload
mensagem = {'context': "vasco",'body': "Enviando mensagem pelo Kafka!"}
topico = "generic"
#print(mensagem)

pubMensKFK(topico, mensagem)

desconectarKFK()

