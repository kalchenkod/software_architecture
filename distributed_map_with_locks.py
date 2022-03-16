import hazelcast
import threading
import time


def counting_function_without_locks(n):
    client = hazelcast.HazelcastClient()
    map = client.get_map("distributed_map_with_locks").blocking()
    key = "key"
    for i in range(1000):
        value = map.get(key)
        # time.sleep(1)
        value += 1
        map.put(key, value)

    print(f"(THREAD {n})Key amount: {map.get(key)}")
    client.shutdown()


def counting_function_with_pessimistic_locks(n):
    client = hazelcast.HazelcastClient()

    map = client.get_map("distributed_map_with_locks").blocking()
    key = "key"
    for i in range(1000):
        map.lock(key)
        try:
            value = map.get(key)
            # time.sleep(1)
            value += 1
            map.put(key, value)
        finally:
            map.unlock(key)

    print(f"(THREAD {n})Key amount: {map.get(key)}")
    client.shutdown()


def counting_function_with_optimistic_locks(n):
    client = hazelcast.HazelcastClient()

    map = client.get_map("distributed_map_with_locks").blocking()
    key = "key"
    for i in range(1000):
        while True:
            old_value = map.get(key)
            # time.sleep(1)
            new_value = old_value
            new_value += 1
            if map.replace_if_same(key, old_value, new_value):
                break

    print(f"(THREAD {n})Key amount: {map.get(key)}")
    client.shutdown()


def initialize_map():
    client = hazelcast.HazelcastClient()
    map = client.get_map("distributed_map_with_locks").blocking()
    map.put('key', 0)
    client.shutdown()


if __name__ == "__main__":
    initialize_map()
    clients = []
    for i in range(3):
        client = threading.Thread(target=counting_function_without_locks, args=(i + 1,))
        clients.append(client)
        client.start()
    for client in clients:
        client.join()

    client = hazelcast.HazelcastClient()
    map = client.get_map("distributed_map_with_locks").blocking()
    print(f"Final Key amount: {map.get('key')}")
    client.shutdown()
