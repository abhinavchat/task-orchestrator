import pika
import json


def publish(channel):
    msg = json.dumps({"name": "Rabbit MQ Tutorial", "message": "Message from producer."})
    channel.basic_publish(exchange='', routing_key='tasks', body=msg)

def main():
    _conn = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    _channel = _conn.channel()
    _channel.queue_declare(queue='tasks')
    publish(_channel)
    _channel.close()
    _conn.close()


if __name__ == "__main__":
    main()
