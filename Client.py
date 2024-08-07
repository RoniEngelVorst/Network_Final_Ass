import threading
import os
from stream import Stream
from connection import Connection
from packet import Packet

def generate_random_bytes(size):
    return os.urandom(size)

def send_stream(stream_id, file_path):
    stream = Stream(stream_id, file_path)
    connection = Connection()
    for packet in stream.read_packet():
        connection.send_packet(packet)
    end_packet = Packet(stream_id, -1, b"END")
    connection.send_packet(end_packet)
    connection.close()
    print(f"Stream {stream_id}: Completed sending {file_path}")

    # Delete the file after sending
    os.remove(file_path)
    print(f"Stream {stream_id}: Deleted file {file_path}")

def main():
    num_of_streams = input("Please enter the number of streams you want: ")
    try:
        num_of_streams = int(num_of_streams)
    except ValueError:
        print("Invalid number of streams. Please enter a valid integer.")
        exit()

    files = []
    data_size = 2 * 1024 * 1024
    for i in range(num_of_streams):
        data = generate_random_bytes(data_size)
        file_name = f"stream_data_{i}.bin"
        files.append(file_name)
        with open(file_name, 'wb') as file:
            file.write(data)
        print(f"Data for stream {i} saved to {file_name}")

    threads = []
    for i, file in enumerate(files):
        thread = threading.Thread(target=send_stream, args=(i, file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
