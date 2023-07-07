package br.imd.messagemanager.listener;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.PublisherBus;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.stereotype.Component;

@Component
public class MosquitoListener implements MqttCallback {
  private static final Logger LOGGER = LogManager.getLogger(MosquitoListener.class);

  private final ObjectMapper objectMapper;
  private final PublisherBus publisherBus;

  public MosquitoListener(ObjectMapper objectMapper, PublisherBus publisherBus) {
    this.objectMapper = objectMapper;
    this.publisherBus = publisherBus;
  }

  @Override
  public void messageArrived(String topic, MqttMessage message) throws Exception {
    final var messageConverted = getMessage(message);
    LOGGER.info("Received message: {}", messageConverted);
    publisherBus.send(messageConverted);
  }

  public void connectionLost(Throwable cause) {
    LOGGER.error("Connection lost!", cause);
  }

  @Override
  public void deliveryComplete(IMqttDeliveryToken token) {
  }

  private MiddlewareMessage getMessage(MqttMessage message) throws JsonProcessingException {
    return objectMapper.readValue(new String(message.getPayload()), MiddlewareMessage.class);
  }
}
