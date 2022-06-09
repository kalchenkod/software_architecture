import requests
import hazelcast
import random
import consul


class Messaging:
    c = consul.Consul(host='localhost', port=8500)

    def __init__(self):
        client = hazelcast.HazelcastClient()
        _, data = self.c.kv.get('mq_name', wait=100)
        self.queue = client.get_queue(data["Value"].decode('utf-8')).blocking()

    def get_messages(self):
        services = self.c.agent.services()
        for service_id in self.c.agent.services():
            if services[service_id]['Service'] == 'messaging_service':
                messaging_services_ip = services[service_id]['Address']
                break

        try:
            response = requests.get(f'http://{messaging_services_ip}:{self.load_balancer()}/message')
            return response.json()
        except:
            return {}

    def write_to_queue(self, msg):
        self.queue.put(msg)

    def load_balancer(self):
        return random.choice(self.get_messaging_service_ports())

    def get_messaging_service_ports(self):
        messaging_service_ports = []
        services = self.c.agent.services()
        for service_id in self.c.agent.services():
            if services[service_id]['Service'] == 'messaging_service':
                messaging_service_ports.append(int(services[service_id]['Port']))
        return messaging_service_ports
