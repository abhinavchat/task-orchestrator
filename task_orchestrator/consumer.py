import pika


def process_tasks(ch, method, properties, body):
    print(f'    [*] Recieved {body}')


def main():
    _conn = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    _channel = _conn.channel()
    _channel.queue_declare(queue='tasks')
    _channel.basic_consume(queue='tasks', on_message_callback=process_tasks, auto_ack=True)
    print('[*] Waiting for tasks. To exit, press CTRL+C')
    _channel.start_consuming()


if __name__ == "__main__":
    main()
