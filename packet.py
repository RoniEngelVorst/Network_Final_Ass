class Packet:
    def __init__(self, stream_id, seq_no, data):
        self.stream_id = stream_id
        self.seq_no = seq_no
        self.data = data

    def encode(self):
        message = f"{self.stream_id},{self.seq_no},{self.data.decode('latin-1')}"
        return message.encode('latin-1')

    @staticmethod
    def decode(data):
        parts = data.decode('latin-1').split(',')
        stream_id = int(parts[0])
        seq_no = int(parts[1])
        data = ','.join(parts[2:]).encode('latin-1')
        return Packet(stream_id, seq_no, data)