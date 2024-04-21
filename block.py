import time
import json


class Block:
    def __init__(self, name):
        self.block = {
            "name": PUF KEY,
            "timestamp": int(time.time())
        }

    def decode(self):
        return json.dumps(self.block)
