import json

import pika

import config
from models import ArticleFullModel
from services import AbstractSkService


class RabbitListener:

    def __init__(self, sk_service: AbstractSkService):
        self._sk_service = sk_service

        self._init_connection()

    def _init_connection(self):
        self._connection_params = pika.URLParameters(config.RABBIT_CONNECT_URL)
        self._connection = pika.BlockingConnection(parameters=self._connection_params)
        self._channel = self._connection.channel()

        self._init_queues()
        self._init_callbacks()

    def _init_queues(self):
        self._channel.queue_declare(queue="business")
        self._channel.queue_declare(queue="accountant")

    def _init_callbacks(self):
        self._channel.basic_consume(on_message_callback=self._new_article_callback('accountant'),
                                    queue='accountant')
        self._channel.basic_consume(on_message_callback=self._new_article_callback('business'),
                                    queue='business')

    def _new_article_callback(self, role: str):
        def callback(ch, method, properties, body):
            try:
                body_data = json.loads(body)[0]
                article = ArticleFullModel(
                    title=body_data['title'],
                    text=body_data['text'],
                    publish_date=body_data['publish_date'],
                    link=body_data['link'],
                    role=role
                )
                self._sk_service.process_article(article)

                ch.basic_ack(delivery_tag=method.delivery_tag)
            except (KeyError, json.decoder.JSONDecodeError):
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print(e)

        return callback

    def run(self):
        print("Start listening")
        self._channel.start_consuming()

    def close(self):
        self._channel.close()
        self._connection.close()
