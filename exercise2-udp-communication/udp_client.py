import socket
import time
import os

# สร้าง UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

# ที่อยู่และพอร์ตของ server (ชื่อ service ใน docker-compose)
server_address = (os.environ.get("SERVER_HOST", "udp_server"), 8080)

# รอให้ server พร้อมเล็กน้อย (depends_on ไม่ได้รอให้โปรแกรมใน container พร้อม)
time.sleep(2)

try:
    message = "Hello from UDP client"
    print("Sending message to server...", flush=True)
    client_socket.sendto(message.encode(), server_address)

    response, server = client_socket.recvfrom(1024)
    print(f"Response from server: {response.decode()}", flush=True)
except Exception as e:
    print(f"An error occurred: {e}", flush=True)
finally:
    client_socket.close()
