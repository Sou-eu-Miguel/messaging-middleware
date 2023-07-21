import json
import configparser

#from publicadorKFK import conectaRKFK, desconectarKFK, pubMensKFK
#from publicadorMQTT import conectarMQTT, desconectarMQTT, iniciarMQTT, pubMensMQTT
#from publicadorRBMQ import desconectarRBMQ, pubMensRBMQ
#import publicadorKFK
#import publicadorMQTT
#import publicadorRBMQ

# VARIAVEIS GLOBAIS
host = ""
port = 0
usuario = ""
senha = ""
topico = ""
vhost = ""
vexchange = ""
vOpcaoMenu = {
                0:"SAIR",
                1:"RABBITMQ",
                2:"KAFKA",
                3:"MQTT",
            }

# FUNÇÕES AUXILIARES PARA CONTROLE DAS
#faz a leitura dos parâmetros de acesso
def importaConfig(provedor):
    config = configparser()
    config.read("publisher-config.ini")
    # 
    port = config.get(provedor,port)
    host = config.get(provedor,host)
    usuario = config.get(provedor,usuario)
    senha = config.get(provedor,senha)
    topico = config.get(provedor,topico)
    vhost = config.get(provedor,vhost)
    vexchange = config.get(provedor,vexchange)


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
    return (json.dumps({"context":pContext,"body":pMsg}).encode("utf-8"))


# #   I N I C I A  O  P R O G R A M A   # #
# Obtem o contexto e mensagem para montagem do payload
print()
vContext = input("Informe o contexto da mensagem: ")
print()
vMsg = input("Digite a mensagem a ser enviada: ")

# monta e apresneta a mensagem escolhida
payload = montaPayload(vContext,vMsg)
print()
print (f"Essa foi a mensagem preparada: {payload}")
print()

# mostra o menu para escolha do destinatário
vDestino = escolheDestino()

print()
print(vOpcaoMenu[vDestino])
print

importaConfig(vOpcaoMenu[vDestino])

print(host,port,)

'''
if vDestino == 3: # MQTT
    "import publicadorMQTT
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
'''