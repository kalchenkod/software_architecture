from flask import Flask
from flask_restful import Api
import consul

from message_app.resources.message_resource import Message

app = Flask(__name__)
api = Api(app)

api.add_resource(Message, "/message")


def get_id(consul_agent):
    if consul_agent.kv.get('services_count')[1] is None:
        consul_agent.kv.put('services_count', '1')
        return '1'
    else:
        index, data = consul_agent.kv.get('services_count', wait=100)
        consul_agent.kv.delete('services_count')
        count = data["Value"].decode('utf-8')
        new_count = str(int(count) + 1)
        consul_agent.kv.put('services_count', new_count)
        return new_count


if __name__ == '__main__':
    c = consul.Consul(host='localhost', port=8500)

    # set message queue name if does not exist
    if c.kv.get('mq_name')[1] is None:
        c.kv.put('mq_name', 'hazelcast_queue')

    # register service
    service_id = get_id(c)
    c.agent.service.register('messaging_service', service_id=service_id, port=5055, address='127.0.0.1')

    # run app
    try:
        app.run(port=5055)
    except:
        c.agent.service.deregister(service_id)
