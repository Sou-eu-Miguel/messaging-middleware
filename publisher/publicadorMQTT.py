import paho.mqtt.client as mqtt
import json

def conectarMQTT (host, port, usuario, senha):
    def ao_conectar(self, client, userdata, rc):
        print("Conectado com o código de retorno: " + str(rc))
        cliente.subscribe(topic=topico)
    
    cliente.on_connect = ao_conectar
    cliente.connect(host, port)


def pubMensMQTT(mensagem):
    msg = json.dumps(mensagem)
    cliente.publish (topico, msg)

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
topico = "geral"
'''

cliente = mqtt.Client()
#iniciar()

#mensagem = "{'contexto':'vasco','mensagem':'tesnte de envio de mensgem pelo MQTT'}"

#publicar_mensagem(mensagem)
#desconectar ()

