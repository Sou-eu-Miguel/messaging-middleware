from kafka import KafkaProducer, KafkaConsumer
import json


def pubMensKFK(nome_topico, mensagem):
    msg=json.dumps(mensagem).encode("utf-8")
    #print(json.loads(msg.decode('utf-8')))
    kafka.send (topic=nome_topico, value=json.loads(msg.decode('utf-8')))
        

# Configurações de conexão
bootstrap_servers = 'localhost:9092'

# Criando uma instância do gerenciador de filas Kafka
#def conectarKFK ():
kafka = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#print(f"Conectado: {kafka.bootstrap_connected}")

# Criando um payload
#mensagem = {'contexto': 'time','mensagem': 'Enviando mensagem pelo Kafka!'}
topico = "geral"
#print(mensagem)

# Publicando uma mensagem no tópico
#kafka.send (topic=topico, value=mensagem)
#publicar_mensagemKFK(topico,mensagem)

# Fechando a conexão
def desconectarKFK():
    kafka.close()
       

