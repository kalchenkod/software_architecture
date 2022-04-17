import requests
import hazelcast
import random


class Messaging:
    messaging_service_ports = [5055, 5059]

    def __init__(self):
        client = hazelcast.HazelcastClient()
        self.queue = client.get_queue("distributed_queue").blocking()

    def get_messages(self):
        port = random.choice(self.messaging_service_ports)
        response = requests.get(f'http://127.0.0.1:{port}/message')
        # if response.status_code != 200:
        #     return
        return response.json()

    def write_to_queue(self, msg):
        self.queue.put(msg)
