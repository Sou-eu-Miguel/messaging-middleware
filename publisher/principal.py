import json
import configparser

#import das funções criadas para os tratamentos das mensagens
#from publicadorKFK import * #conectaRKFK, desconectarKFK, pubMensKFK
#from publicadorMQTT import * #conectarMQTT, desconectarMQTT, iniciarMQTT, pubMensMQTT
#from publicadorRBMQ import * #desconectarRBMQ, pubMensRBMQ
#import publicadorKFK
import publicadorMQTT_novo as pubMQTT
import publicadorRBMQ_novo as pubRBMQ
import publicadorKFK_novo as pubKFK

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
def importar_config(secao):
    config = configparser.ConfigParser(delimiters="=")
    config.read("publisher-config.ini")
    #
    host = config.get(secao,"host")
    port = config.get(secao,"port")
    usuario = config.get(secao,"usuario")
    senha = config.get(secao,"senha")
    if secao != "RABBITMQ":
        topico = config.get(secao,"topico")
    if secao == "RABBITMQ":
        vhost =  config.get(secao,"vhost")
        vexchange = config.get(secao,"vexchange")

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

#importar as configurações de acesso
importar_config(vOpcaoMenu[vDestino])

print(vOpcaoMenu[vDestino])
print(host,port,usuario,senha,topico)

if vDestino == 1: # RABBITMQ
    try:
        #pubRBMQ.conectarRBMQ(host=host,port=port,user=usuario,passwd=senha,vhost=vhost)
        pubRBMQ.pubMensRBMQ(mensagem=payload,pExchange=vexchange)
        pubRBMQ.desconectarMQTT()
        print (f"Mensagem enviadao com sucesso para a fila do {vOpcaoMenu[vDestino]}")
    except SystemError as err:
        print(f"Ocorreu o erro {err} e a mensagem não foi enviada!")
elif vDestino == 2: # KAFKA
    try:
        pubKFK.conectarKFK(f"{host}:{port}")
        pubKFK.pubMensKFK(topico=topico,mensagem=payload)
        pubKFK.desconectarKFK()
        print (f"Mensagem enviadao com sucesso para a fila do {vOpcaoMenu[vDestino]}")
    except SystemError as err:
        print(f"Ocorreu o erro {err} e a mensagem não foi enviada!")
elif vDestino == 3: # MQTT  
    try:
        pubMQTT.conectarMQTT(host,port,usuario,senha,topico)
        pubMQTT.iniciarMQTT()
        pubMQTT.pubMensMQTT(mensagem=payload,pTopico=topico)
        pubMQTT.desconectarMQTT()
        print (f"Mensagem enviadao com sucesso para a fila do {vOpcaoMenu[vDestino]}")
    except SystemError as err:
        print(f"Ocorreu o erro {err} e a mensagem não foi enviada!")
else:
    print("Finalizado!!!")