import socket

HOST = '127.0.0.1'
PORT = 6000

def start_udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"UDP сервер запущен на {HOST}:{PORT}")

        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode()
            print(f"Получено от {addr}: {message}")

            if message.lower() == 'exit':
                print("Клиент завершил соединение. Сервер останавливается.")
                break

            s.sendto(data, addr)  # отправляем обратно как эхо

if __name__ == '__main__':
    start_udp_server()
