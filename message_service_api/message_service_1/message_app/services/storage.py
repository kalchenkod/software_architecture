import hazelcast
import threading


class Storage:
    messages = []

    def __init__(self):
        client = hazelcast.HazelcastClient()
        self.queue = client.get_queue("distributed_queue").blocking()
        reader = threading.Thread(target=self.read_from_queue, args=())
        reader.start()

    def get_all(self):
        return ",".join(self.messages)

    def read_from_queue(self):
        while True:
            msg = self.queue.take()
            print(msg)
            self.messages.append(msg)
