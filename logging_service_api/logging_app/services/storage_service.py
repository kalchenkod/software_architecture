class Storage:
    hash_table = {}

    def store(self, uuid, message):
        self.hash_table[uuid] = message

    def get_all(self):
        return ",".join(self.hash_table.values())
