import random
from packet import Packet

def random_grill():
    return random.randint(1000, 2000)

class Stream:
    def __init__(self, stream_id, file_path):
        self.stream_id = stream_id
        self.file_path = file_path
        self.packet_size = random_grill()
        self.seq_no = 0

    def read_packet(self):
        with open(self.file_path, 'rb') as file:
            while True:
                data = file.read(self.packet_size)
                if not data:
                    break
                yield Packet(self.stream_id, self.seq_no, data)
                self.seq_no += 1