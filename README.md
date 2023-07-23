# PROJETO FINAL DA DISCIPLINA PPGTI1009 - PROGRAMAÇÃO DISTRIBUÍDA
### DISCENTE: Frederico Araújo da Silva Lopes

## Objetivo
O presente projeto visa apresentar a construção de uma solução para a implementação de três serviços de mensageria, utilizando MQTT, KAFKA e RABBITMQ, onde:
* Há aplicação(ões) para produção e consumo de mensagens
* As aplicações que forneçam e consumam filas, mas cada uma só trabalha com 1 tipo de mensageria
* O middleware deverá ser um serviço de gerenciamento de mensageria que leia todas as filas e direcionem as mensagens de uma fila para o destinatário
* Cada serviço de mensageria deverá possuir uma fila ou tópico GERAL, que receberá as mensagem dos produtores
* Cada serviço de mensageria terá um ou vários filas ou tópicos para os consumidores dos serviços de mensageria. contexto: fila ou tópico
* O gerenciador de serviços
  * deve possuir um gestor de mensagerias (brokers)
  * deve ter um serviço que identifique os contexto da mensagem gerais (parser)
  * deve ter um serviço que processe as mensagens aos seus destinatário

### Uma visão geral da infraestrtura

![Serviço de mensageria](https://github.com/Sou-eu-Miguel/messaging-middleware/assets/56575639/8e5203a4-8c8f-4560-ba8b-fafcecf5e02d)
