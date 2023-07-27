import paho.mqtt.client as mqtt
import json
import configparser

# Configurações de conexão
'''
host = 'localhost'
port = 1883
usuario = 'guest'
senha = 'guest'
topico = "generic"
'''

#importar as configurações de acesso
config = configparser.ConfigParser(delimiters="=")
config.read("publisher-config.ini")
host = config.get("MQTT","host")
port = int(config.get("MQTT","port"))
usuario = config.get("MQTT","usuario")
senha = config.get("MQTT","senha")
topico = config.get("MQTT","topico")

#print(f"Parâmetros lidos: {host}:{port}, user:{usuario} e tópico:{topico}\n")


def conectarMQTT (host, port, usuario, senha):
    def ao_conectar(self, client, userdata, rc):
        #print("Conectado com o código de retorno: " + str(rc))
        cliente.subscribe(topic=topico)
        return (rc)
    
    cliente.on_connect = ao_conectar
    cliente.connect(host, port)
    #return (cliente)


def pubMensMQTT(mensagem,pTopico):
    #msg = json.dumps(mensagem).encode("utf-8")
    #cliente.publish (topico, msg)
    #json.dumps({"context":pContext,"body":pMsg}).encode("utf-8")
    cliente.publish (pTopico, mensagem)


def iniciarMQTT():
    cliente.loop()


def desconectarMQTT():
    cliente.disconnect()

def montaPayload (pContext, pMsg):
    return (json.dumps({"context":pContext,"body":pMsg}).encode("utf-8"))
    #return ({"context":pContext,"body":pMsg})

cliente = mqtt.Client()


#cliente = conectarMQTT(host,int(port),usuario,senha,topico)
conectarMQTT(host,port,usuario,senha)

iniciarMQTT()

#mensagem = "{'context':'vasco','body':'tesnte de envio de mensgem pelo MQTT'}"

print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Digite a mensagem a ser enviada: ")

# monta e apresenta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()


#pubMensMQTT("{'context':'vasco','body':'tesnte de envio de mensgem pelo MQTT'}",topico)
pubMensMQTT(payload,topico)
print("Mensagem enviada para a fila do MQTT!!")
desconectarMQTT ()

