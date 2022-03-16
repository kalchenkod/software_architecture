import hazelcast
import threading
import time


def writer_client():
    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed_queue").blocking()
    value = 0
    max_size = 0
    while value < 1000:
        max_size = max(max_size, queue.size())
        if queue.size() >= 800:
            continue
        queue.put(value)
        value += 1

    print(f"(WRITER) Finished. Written to queue {max_size}")
    client.shutdown()


def reader_client(n):
    time.sleep(5)
    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed_queue").blocking()
    read = 0
    while True:
        if queue.poll(5):
            read += 1
        else:
            break

    print(f"(READER {n}) Finished. Read {read}")
    client.shutdown()


if __name__ == "__main__":
    clients = []
    for i in range(3):
        if i:
            client = threading.Thread(target=reader_client, args=(i,))
        else:
            client = threading.Thread(target=writer_client, args=())
        clients.append(client)
        client.start()
    for client in clients:
        client.join()

    client = hazelcast.HazelcastClient()
    queue = client.get_queue("distributed_queue").blocking()
    print(f"Final queue size: {queue.size()}")
    client.shutdown()


