package br.imd.messagemanager.publisher;

import br.imd.messagemanager.model.MiddlewareMessage;

public interface Publisher {

  void send(MiddlewareMessage message);
}
