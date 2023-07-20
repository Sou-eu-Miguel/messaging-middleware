import json
import configparser

from publicadorKFK import conectaRKFK, desconectarKFK, pubMensKFK
from publicadorMQTT import conectarMQTT, desconectarMQTT, iniciarMQTT, pubMensMQTT
from publicadorRBMQ import desconectarRBMQ, pubMensRBMQ

# replica o caracter a quantdade de vezes desejada
def repl(c, v):
    ret = ""
    for x in range(v):
        ret += c
    return (ret)

# monta o menu e retorna a opção escolhida para envio da mensagem
def escolheDestino():
    #clear
    vMenu = {


        
        0:"Sair do Sistema", 
        1:"Enviar mensagem para RabbitMq", 
        2:"Enviar mensagem para Kafka",
        3:"Enviar mensagem para MQTT" 
            }
    print (repl("=",40))
    for x in range(len(vMenu)):
        print (f"|=> {x} - {vMenu[x]}")
    print (repl("-",40))
    print ("Escolha o número dentre as opções do menu: ")
    try:
        vOpt = int(input(""))
        while vOpt not in vMenu.keys():
            print ("Escolha o número dentre as opções do menu.")
            vOpt = int(input(""))
        return (vOpt)
    except:
        return(0)
    

def montaPayload (pContext, pMsg):
    return ({
        "contexto": pContext, 
        "mensagem": pMsg
            })    

# Obtem o contexto e mensagem para montagem do payload
print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Informe a mensagem a ser enviada: ")

# monta e apresneta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()

#faz a leitura dos parâmetros de acesso
def importar_config(provedor):
    #seta o arquivo de configuraçao
    config = ConfigParser()
    config.read("publisher-config.ini")
    # faz a leitua dos dados do arquivo de configuracao
    port = config.get(provedor,port)
    host = config.get(provedor,host)
    usuario = config.get(provedor,usuario)
    senha = config.get(provedor,senha)
    topico = config.get(provedor,topico)


vDestino = escolheDestino()

#Variáveis para uso nas conexões
host="localhost"
port=8080
usuario="guest"
senha="guest"
topico="middleware" 



if vDestino == 3: # MQTT
    import publicadorMQTT
    importar_config("MQTT")
    conectarMQTT('localhost',1883,'guest','guest')
    iniciarMQTT()
    pubMensMQTT(payload)
    desconectarMQTT()
elif vDestino == 2: # KAFKA
    import publicadorKFK
    
    pubMensKFK(topico,payload)
    desconectarKFK()
elif vDestino == 2: # RABBITMQ
    import publicadorRBMQ

    pubMensRBMQ(payload)
    desconectarRBMQ
