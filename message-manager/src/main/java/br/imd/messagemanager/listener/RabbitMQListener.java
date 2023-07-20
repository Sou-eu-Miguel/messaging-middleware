package br.imd.messagemanager.listener;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.PublisherBus;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Component
public class RabbitMQListener {
  private static final Logger LOGGER = LogManager.getLogger(RabbitMQListener.class);

  private final PublisherBus publisherBus;

  public RabbitMQListener(PublisherBus publisherBus) {
    this.publisherBus = publisherBus;
  }

  @RabbitListener(queues = "#{channelProperty.generic.name()}")
  public void handler(@Payload MiddlewareMessage message) {
    LOGGER.info("Received message: {}", message);
    publisherBus.send(message);
  }
}
