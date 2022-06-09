import requests
import random
import consul


class Logging:
    c = consul.Consul(host='localhost', port=8500)

    def log(self, uuid, message):
        services = self.c.agent.services()
        for service_id in services:
            if services[service_id]['Service'] == 'logging_service':
                logging_services_ip = services[service_id]['Address']
                break

        try:
            response = requests.post(f'http://{logging_services_ip}:{self.load_balancer()}/logging',
                                     json={"uuid": uuid, "msg": message})
            return response.json()
        except:
            return {}

    def get_messages(self):
        services = self.c.agent.services()
        for service_id in self.c.agent.services():
            if services[service_id]['Service'] == 'logging_service':
                logging_services_ip = services[service_id]['Address']
                logging_services_port = services[service_id]['Port']
                break
        try:
            response = requests.get(f'http://{logging_services_ip}:{logging_services_port}/logging')
            return response.json()
        except:
            return {}

    def load_balancer(self):
        return random.choice(self.get_logging_service_ports())

    def get_logging_service_ports(self):
        logging_service_ports = []
        services = self.c.agent.services()
        for service_id in self.c.agent.services():
            if services[service_id]['Service'] == 'logging_service':
                logging_service_ports.append(int(services[service_id]['Port']))
        return logging_service_ports
