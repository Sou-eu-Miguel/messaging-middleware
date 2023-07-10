from kafka import KafkaConsumer

bootstrap_servers = ['localhost:9092']
consumer_group_id = 'sample'
topic = 'test-topic'

consumer = KafkaConsumer(topic, group_id=consumer_group_id, bootstrap_servers=bootstrap_servers)

def main():
    for message in consumer:
        print("{}".format(message))

    consumer.close()

if __name__ == '__main__':
    main()