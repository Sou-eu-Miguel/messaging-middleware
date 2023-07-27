# Procedimentos para executar as aplicações

## Subindo os ambientes

O Sistema é composto dos módulos indicados abaixo que deverão ser executados na ordem.<br>
O acesso deverá ser realizado a partir de uma máquina virtual, que contenha o projeto baixado ou, conforme o caso, baixar o projeto a partir deste projeto do Github, devendo-se abrir um prompt de comando para executar o passo a passo.

* **1ª etapa**: Subir os serviços de mensageria<br>
  Para inicializar os serviços de mensageria, é necessário subir os containeres, conforme segue:

  ```shell
  # mudar o diretório para o correspondente
  message-midleware$ cd docker
  # caso tenha instaldo o docker-compose
  message-midleware/docker$ ./creaeContainer.sh
  # ou, caso não tenha o docker-compose, mas tão somente o docker
  message-midleware/docker$ ./creaeContainerUbuntu.sh
  ```
* **2ª etapa**: Executar o Gerenciador de filas<br>
  Esse serviço é necessário para carregar as configurações dos serviços de mensageria e só é necessário executar uma primeira e única vez, se os containeres estiverem configurados para persistir os dados via nfs, o que é recomendado.

```shell
  # mudar o diretório para o correspondente
  message-midleware/docker$ cd ../queue-manager
  # Executar o bootRun
  message-midleware/queue-manager$ ./gradlew bootRun 
  ```

  Ao concluir a execução, a aplicação poderá ser echada, através do conjunto de teclas CTRL+C e a verificação sobre a criação das configurações iniciais podem ser realziadas atavés do gerenciador gráfico do RabbitMQ e Kafka.

* **3ª etapa**: Executar o gerenciador de mensagens<br>
  Esse serviço é responsável por ler as mensagens enviadas às filas de contexto geral, tratar e distribuir para o serviço de mensageria adequado.

  ```shell
  # mudar o diretório para o correspondente
  message-midleware/queue-manager$ cd ../message-manager
  # Executar o bootRun
  message-midleware/message-manager$ ./gradlew bootRun 
  ```
  
* **4ª etapa**: Enviar as mensagens<br>
  As configurações dos acessos aos serviços de mensageria estão dispotos no arquivo **_publisher-config.ini_** e será lido, conforme a escolha de envio da mensagem.<br>
  O envio das mensagens foi criado através de script python, devendo ser executado conforme o caso:

  ```
  # mudar o diretório para o correspondente
  message-midleware/queue-manager$ cd ../publisher
  # Enviar mensagens para qualquer dos serviços
  message-midleware/publisher$ python principal.py
  ```
  
  Deverá ser informado o contexto e o teor da mensagem, em seguida deverá ser encolhido serviço de mensageria a ser utilizado para envio da mensagem.

* **5ª etapa**: Consumir ou receber as mensagens<br>
  As mensagens serão consumidas das filas, conforme a chamada de uma das filas, conforme indicado abaixo:
  
  ```
  # mudar o diretório para o correspondente
  message-midleware/publisher$ cd ../subscriber
  # Consumir mensagens do RabbitMq
  message-midleware/publisher$ python script_rabbitmq_sub.py
  # Consumir mensagens do Kafka
  message-midleware/publisher$ python script_kafka_sub.py
  # Consumir mensagens do Mqtt
  message-midleware/publisher$ python script_mqtt_sub.py
  ```
  
