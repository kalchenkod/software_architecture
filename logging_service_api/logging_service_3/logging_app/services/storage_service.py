import hazelcast


class Storage:
    def __init__(self):
        self.client = hazelcast.HazelcastClient()
        self.map = self.client.get_map("distributed_map").blocking()

    def store(self, uuid, message):
        self.map.put(uuid, message)

    def get_all(self):
        return ",".join(self.map.values())
