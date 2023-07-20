package br.imd.messagemanager.listener;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.PublisherBus;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class KafkaGenericListener {
  private static final Logger LOGGER = LogManager.getLogger(MosquitoListener.class);
  private final ObjectMapper objectMapper;
  private final PublisherBus publisherBus;

  public KafkaGenericListener(ObjectMapper objectMapper, PublisherBus publisherBus) {
    this.objectMapper = objectMapper;
    this.publisherBus = publisherBus;
  }

  @KafkaListener(topics = "#{channelProperty.generic.name()}", groupId = "#{channelProperty.generic.name()}")
  public void receiveMessage(String message) throws JsonProcessingException {
    final var middlewareMessage = objectMapper.readValue(message, MiddlewareMessage.class);
    LOGGER.info("Received message: {}", message);
    publisherBus.send(middlewareMessage);
  }
}

