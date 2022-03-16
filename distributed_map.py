import hazelcast

client = hazelcast.HazelcastClient()

map = client.get_map("distributed_map")
for i in range(1000):
    map.put_if_absent(i, f"value {i}")

client.shutdown()