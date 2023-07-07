package br.imd.messagemanager.publisher;

import br.imd.messagemanager.model.MiddlewareMessage;
import java.util.List;
import org.springframework.stereotype.Component;

@Component
public class PublisherBus {

  private final List<Publisher> publishers;

  public PublisherBus(List<Publisher> publishers) {
    this.publishers = publishers;
  }

  public void send(MiddlewareMessage message) {
    publishers.forEach(publisher -> publisher.send(message));
  }
}
