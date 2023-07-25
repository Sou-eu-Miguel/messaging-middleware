#!pip install kafka
#!pip install kafka-python


from kafka import KafkaProducer, KafkaConsumer
import json

class GerenciadorFilaKafka:
    def __init__(self, pServer):
        self.producer = KafkaProducer(bootstrap_servers=pServer)
        self.consumer = KafkaConsumer(bootstrap_servers=pServer)

    def criar_topico(self, pTopico):
        # Nenhuma ação necessária para criar um tópico no Kafka
        print (f"Tópico {pTopico} criado.")

    def publicar_mensagemKFK(self, pTopico, pMensagem):
        self.producer.send(pTopico, value=pMensagem)

    def consumir_topico(self, pTopico, pRetorno):
        self.consumer.subscribe([pTopico])
        for mensagem in self.consumer:
            payload = mensagem.value
            retorno(payload)

    def fechar_conexao(self):
        self.producer.close()
        self.consumer.close()
        

#Definindo as rotinas de criação e consumo das filas - Kafka        
def retorno(payload):
    contexto = payload["context"]
    #destinatario = payload["body"]
    mensagem = payload["body"]
    #print(f"Recebido: Contexto: {contexto}, Destinatário: {destinatario}, Mensagem: {mensagem}")
    print(f"Recebido: Contexto: {contexto}, Mensagem: {mensagem}")

# Configurações de conexão
bootstrap_servers = 'localhost:9092'

# Criando uma instância do gerenciador de filas Kafka
gfKafka = GerenciadorFilaKafka(bootstrap_servers)

# Criando um tópico
gfKafka.criar_topico('DISTRIB')

# Criando um payload
payload = {
    "context": "geral",
    "body": "Enviando mensagem pelo Kafka!"
}

# Publicando uma mensagem no tópico
gfKafka.publicar_mensagem('DISTRIB', payload)

# Consumindo o tópico
gfKafka.consumir_topico('DISTRIB', retorno)

# Fechando a conexão
gfKafka.fechar_conexao()
       
