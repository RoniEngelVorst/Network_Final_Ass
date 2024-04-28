import socket
import threading


def udp_client(stream_id, messages, server_address=("127.0.0.1", 9999)):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i, msg in enumerate(messages):
        message = f"{stream_id},{i},{msg}"
        print(f"Stream {stream_id}: Sending {msg}")
        client_socket.sendto(message.encode(), server_address)
        data, _ = client_socket.recvfrom(1024)
        print(f"Stream {stream_id}: Server replied: {data.decode()}")

    client_socket.close()


def main():
    print("main function begin receiver side")
    messages1 = ["Hello", "World", "from", "stream 1!"]
    messages2 = ["Another", "stream", "here", "stream 2!"]

    thread1 = threading.Thread(target=udp_client, args=(1, messages1))
    thread2 = threading.Thread(target=udp_client, args=(2, messages2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()