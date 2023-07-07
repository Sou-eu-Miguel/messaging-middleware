package br.imd.messagemanager.publisher.impl;

import br.imd.messagemanager.model.MiddlewareMessage;
import br.imd.messagemanager.publisher.Publisher;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.nio.charset.StandardCharsets;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

@Component
public class PublisherMqtt implements Publisher {

  private final MqttClient mqttClient;
  private final ObjectMapper objectMapper;

  public PublisherMqtt(@Lazy MqttClient mqttClient, ObjectMapper objectMapper) {
    this.mqttClient = mqttClient;
    this.objectMapper = objectMapper;
  }

  @Override
  public void send(MiddlewareMessage message) {
    try {
      final var context = message.context();
      final var body = message.body();
      final String payload = objectMapper.writeValueAsString(body);
      final var mqttMessage = new MqttMessage(payload.getBytes(StandardCharsets.UTF_8));
      mqttClient.publish(context, mqttMessage);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }
}
