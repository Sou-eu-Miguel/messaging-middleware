import paho.mqtt.client as mqtt
import json
import configparser


cliente = mqtt.Client()

def conectarMQTT (host, port, usuario, senha,topico):
    def ao_conectar(self, cliente, userdata, rc):
        print("Conectado com o código de retorno: " + str(rc))
        cliente.subscribe(topic=topico)
        return (rc)
    
    cliente.on_connect = ao_conectar
    cliente.connect(host, port)
    #return (cliente)


def pubMensMQTT(mensagem,pTopico):
    msg = json.dumps(mensagem).encode("utf-8")
    #cliente.publish (topico, msg)
    #json.dumps({"context":pContext,"body":pMsg}).encode("utf-8")
    cliente.publish (pTopico, mensagem)

def iniciarMQTT():
    cliente.loop()

def desconectarMQTT():
    cliente.disconnect()



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
port = config.get("MQTT","port")
usuario = config.get("MQTT","usuario")
senha = config.get("MQTT","senha")
topico = config.get("MQTT","topico")

print(host,port,usuario,senha,topico)

#cliente = conectarMQTT(host,int(port),usuario,senha,topico)
conectarMQTT(host,int(port),usuario,senha,topico)

iniciarMQTT()

#mensagem = "{'context':'vasco','body':'tesnte de envio de mensgem pelo MQTT'}"

pubMensMQTT("{'context':'vasco','body':'tesnte de envio de mensgem pelo MQTT'}",topico)
print("Mensagem enviada!!")
desconectarMQTT ()

