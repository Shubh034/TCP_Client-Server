import socket

def send_data(message):
    HOST = "127.0.0.1"
    PORT = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall(message.encode("utf-8"))
    response = client_socket.recv(1024)

    print("Server response:", response.decode("utf-8"))
    client_socket.close()

if __name__ == "__main__":
    send_data("Hello from TCP client!")
