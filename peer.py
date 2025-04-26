
import socket
import threading
from secure_utils import decrypt

def handle_client(conn, addr):
    try:
        print(f"[Connection from {addr}]")
        encrypted_msg = conn.recv(1024)
        message = decrypt(encrypted_msg)
        print(f"[Message]: {message}")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen()
    print(f"[Listening] on port {port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

def main():
    port = int(input("Your listening port: "))
    threading.Thread(target=start_server, args=(port,), daemon=True).start()

    from secure_utils import encrypt

    while True:
        try:
            ip = input("Target IP: ")
            target_port = int(input("Target Port: "))
            message = input("Message: ")

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, target_port))
            client.send(encrypt(message))
            client.close()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
