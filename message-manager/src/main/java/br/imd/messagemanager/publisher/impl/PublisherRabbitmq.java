package br.imd.messagemanager.publisher.impl;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.Publisher;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
public class PublisherRabbitmq implements Publisher {

  private static final String SPECIFIC = "specific";

  private final RabbitTemplate rabbitTemplate;

  public PublisherRabbitmq(RabbitTemplate rabbitTemplate) {
    this.rabbitTemplate = rabbitTemplate;
  }

  @Override
  public void send(MiddlewareMessage message) {
    final var context = message.context();
    final var body = message.body();
    rabbitTemplate.convertAndSend(SPECIFIC, context, body);
  }
}
