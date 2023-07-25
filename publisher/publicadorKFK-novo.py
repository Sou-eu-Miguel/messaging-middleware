from kafka import KafkaProducer
import json
import configparser

kfk=KafkaProducer()

def pubMensKFK(topico, mensagem):
    msg=json.dumps(mensagem).encode("utf-8")
    kfk.send (topico, msg)
        

# Configurações de conexão
# importar as configurações de acesso
config = configparser.ConfigParser(delimiters="=")
config.read("publisher-config.ini")
host = config.get("KAFKA","host")
port = config.get("KAFKA","port")
usuario = config.get("KAFKA","usuario")
senha = config.get("KAFKA","senha")
topico = config.get("KAFKA","topico")


# Criando uma instância do gerenciador de filas Kafka
def conectarKFK (pServer):
    kfk = KafkaProducer(bootstrap_servers=pServer)
# Fechando a conexão
def desconectarKFK():
    kfk.close()
       
#print(host,port,usuario,senha,topico)
# iniciando o kafka
vServer = host+':'+ str(port) 
print(vServer)
print (host+':'+ str(port))


conectarKFK(f"{host}:{port}")


# Criando um payload
#mensagem = {'context': "vasco",'body': "Enviando mensagem pelo Kafka!"}
#topico = "generic"
#print(mensagem)

#pubMensKFK(topico, mensagem)
pubMensKFK(topico, {'context': "vasco",'body': "Enviando mensagem pelo Kafka!"})
print("Mensagem enviada!!")

desconectarKFK()

