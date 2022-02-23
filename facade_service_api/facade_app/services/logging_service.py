import requests


class Logging:
    @staticmethod
    def log(uuid, message):
        response = requests.post('http://127.0.0.1:5056/logging', json={"uuid": uuid,
                                                                        "msg": message})
        # if response.status_code != 200:
        #     return
        return response.json()

    @staticmethod
    def get_messages():
        response = requests.get('http://127.0.0.1:5056/logging')
        # if response.status_code != 200:
        #     return
        return response.json()
