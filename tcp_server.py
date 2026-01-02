print("Server file started")


import socket
import psycopg2

# PostgreSQL connection
DB_CONFIG = {
    "host": "localhost",
    "dbname": "tcp_app",
    "user": "postgres",
    "password": "270403",
    "port": 5432
}

def save_to_db(message):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO received_data (message) VALUES (%s)",
        (message,)
    )
    conn.commit()
    cur.close()
    conn.close()

def start_server():
    HOST = "127.0.0.1"
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"TCP Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024)
        if data:
            message = data.decode("utf-8")
            print(f"Received: {message}")

            save_to_db(message)
            client_socket.sendall(b"Data stored successfully")

        client_socket.close()

if __name__ == "__main__":
    start_server()
