import json
import configparser

#import das funções criadas para os tratamentos das mensagens
#from publicadorKFK import * #conectaRKFK, desconectarKFK, pubMensKFK
#from publicadorMQTT import * #conectarMQTT, desconectarMQTT, iniciarMQTT, pubMensMQTT
#from publicadorRBMQ import * #desconectarRBMQ, pubMensRBMQ

# VARIÁVEIS GLOBAIS
host = ""
port = 0
usuario = ""
senha = ""
topico = ""
vhost =  ""
vexchange = ""
vOpcaoMenu = {0:"SAIR",
              1:"RABBITMQ",
              2:"KAFKA",
              3:"MQTT"}

# FUNÇÕES DE CONFIGURAÇÃO E AUXILIARES
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
    
# prepara a mensagem já no formato JSON
def montaPayload (pContext, pMsg):
    return (json.dumps({"context":pContext,"body":pMsg}).encode("utf-8"))

# faz a leitura do arquivo de parâmetros de acesso para cada servidor
def importar_config(provedor):
    config = configparser()
    config.read("publisher-config.ini")
    #
    host = config.get(provedor,host)
    port = config.get(provedor,port)
    usuario = config.get(provedor,usuario)
    senha = config.get(provedor,senha)
    topico = config.get(provedor,topico)
    vhost =  config.get(provedor,vhost)
    vexchange = config.get(provedor,vexchange)

# INÍCIO DO PROGRAMA PROPRIMENTE DITO

# Obtem o contexto e mensagem para montagem do payload
print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Digite a mensagem a ser enviada: ")

# monta e apresenta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()

# Selecionar entre as opções para envio da mensagem
vDestino = escolheDestino()

print(vOpcaoMenu[vDestino])

'''if vDestino == 3: # MQTT
    
    importar_config("MQTT")
    conectarMQTT('localhost',1883,'guest','guest')
    iniciarMQTT()
    pubMensMQTT(payload)
    desconectarMQTT()
elif vDestino == 2: # KAFKA
    
    
    pubMensKFK(topico,payload)
    desconectarKFK()
elif vDestino == 2: # RABBITMQ
    pubMensRBMQ(payload)
    desconectarRBMQ
'''