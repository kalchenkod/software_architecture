import requests


class Messaging:
    @staticmethod
    def get_message():
        response = requests.get('http://127.0.0.1:5055/message')
        # if response.status_code != 200:
        #     return
        return response.json()
