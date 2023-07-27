from kafka import KafkaProducer
import json
import configparser

kfk=KafkaProducer()

def pubMensKFK(topico, mensagem):
    #msg=json.dumps(mensagem).encode("utf-8")
    kfk.send (topico, mensagem)
        

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

def montaPayload (pContext, pMsg):
    return (json.dumps({"context":pContext,"body":pMsg}).encode("utf-8"))
    #return ({"context":pContext,"body":pMsg})
       
#print(host,port,usuario,senha,topico)
# iniciando o kafka
#vServer = host+':'+ str(port) 
#print(vServer)
#print (host+':'+ str(port))


# Criando um payload
#mensagem = {'context': "vasco",'body': "Enviando mensagem pelo Kafka!"}
#topico = "generic"
#print(mensagem)

print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Digite a mensagem a ser enviada: ")

# monta e apresenta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()

#pubMensKFK(topico, mensagem)
conectarKFK(f"{host}:{port}")
pubMensKFK(topico, payload)
print("Mensagem enviada!!")
desconectarKFK()

