class UUIDGeneration:
    uuid = 0

    @staticmethod
    def generate_uuid():
        UUIDGeneration.uuid += 1
        return UUIDGeneration.uuid
