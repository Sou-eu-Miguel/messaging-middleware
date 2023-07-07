package br.imd.messagemanager.listener;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.PublisherBus;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Component
public class RabbitMQListener {

  private final PublisherBus publisherBus;

  public RabbitMQListener(PublisherBus publisherBus) {
    this.publisherBus = publisherBus;
  }

  @RabbitListener(queues = "#{channelProperty.generic.name()}")
  public void handler(@Payload MiddlewareMessage message) {
    publisherBus.send(message);
  }
}
