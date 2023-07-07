package br.imd.messagemanager.publisher.impl;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.Publisher;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class PublisherKafka implements Publisher {

  private final ObjectMapper objectMapper;
  private final KafkaTemplate<String, String> kafkaTemplate;

  public PublisherKafka(ObjectMapper objectMapper, KafkaTemplate<String, String> kafkaTemplate) {
    this.objectMapper = objectMapper;
    this.kafkaTemplate = kafkaTemplate;
  }

  @Override
  public void send(MiddlewareMessage message) {
    try {
      final var context = message.context();
      final var body = message.body();
      kafkaTemplate.send(context, objectMapper.writeValueAsString(body));
    } catch (JsonProcessingException e) {
      throw new RuntimeException(e);
    }
  }
}
