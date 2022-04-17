import requests
import random


class Logging:
    logging_service_ports = [5056, 5057, 5058]

    def log(self, uuid, message):
        response = requests.post(f'http://127.0.0.1:{self.load_balancer()}/logging', json={"uuid": uuid,
                                                                                           "msg": message})

        return response.json()

    @staticmethod
    def get_messages():
        response = requests.get('http://127.0.0.1:5056/logging')
        # if response.status_code != 200:
        #     return
        return response.json()

    def load_balancer(self):
        return random.choice(self.logging_service_ports)
