import hazelcast
import threading
import consul


class Storage:
    c = consul.Consul(host='localhost', port=8500)
    messages = []

    def __init__(self):
        client = hazelcast.HazelcastClient()
        _, data = self.c.kv.get('mq_name', wait=100)
        self.queue = client.get_queue(data["Value"].decode('utf-8')).blocking()
        reader = threading.Thread(target=self.read_from_queue, args=())
        reader.start()

    def get_all(self):
        return ",".join(self.messages)

    def read_from_queue(self):
        while True:
            msg = self.queue.take()
            print(msg)
            self.messages.append(msg)
