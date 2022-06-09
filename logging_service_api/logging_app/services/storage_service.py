import hazelcast
import consul


class Storage:
    c = consul.Consul(host='localhost', port=8500)

    def __init__(self):
        self.client = hazelcast.HazelcastClient()
        _, data = self.c.kv.get('mq_name', wait=100)
        self.map = self.client.get_map(data["Value"].decode('utf-8')).blocking()

    def store(self, uuid, message):
        self.map.put(uuid, message)

    def get_all(self):
        return ",".join(self.map.values())
