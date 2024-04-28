import socket
import threading
import random
import os

def generate_random_bytes(size):
    # Generate 'size' number of random bytes
    return os.urandom(size)


def random_grill():
    # Generate a random integer between 1000 and 2000, inclusive
    return random.randint(1000, 2000)




def handle_client(server_socket):
    while True:
        data, addr = server_socket.recvfrom(1024)
        if data:
            stream_id, seq_no, message = parse_message(data)
            print(f"Stream {stream_id}: Received message {seq_no} - {message} from {addr}")
            reply = f"Received message {seq_no} on stream {stream_id}".encode()
            server_socket.sendto(reply, addr)


def parse_message(data):
    parts = data.decode().split(',')
    stream_id = int(parts[0])
    seq_no = int(parts[1])
    message = ','.join(parts[2:])
    return stream_id, seq_no, message


def main():
    # getting an input from the user in order to define how many streams we want
    num_of_streams = input("Please enter the number of streams you want: ")

    # Convert the input to an integer
    try:
        num_of_streams = int(num_of_streams)
    except ValueError:
        print("Invalid number of streams. Please enter a valid integer.")
        # Optionally, you can add error handling such as exiting the program or asking again
        exit()

    # creating an array of files
    files = []
    data_size = random_grill()
    for i in range(num_of_streams):
        data = generate_random_bytes(data_size)
        files.append(data)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 9999))
    print("UDP server up and listening")
    server_thread = threading.Thread(target=handle_client, args=(server_socket,))
    server_thread.start()


if __name__ == '__main__':
    main()