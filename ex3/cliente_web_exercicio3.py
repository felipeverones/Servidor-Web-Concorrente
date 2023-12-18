import socket
from threading import Thread

num_clients = 50  # Número de clientes simultâneos
total_requests = 0

# Função para enviar uma requisição e receber a resposta
def send_request_and_get_response(path):
    global total_requests

    # Cria um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Conecta ao servidor
        client_socket.connect(('127.0.0.1', 2023))
        # Monta a requisição HTTP GET
        request = f'GET {path} HTTP/1.1\r\nHost: localhost:2023\r\n\r\n'
        # Envia a requisição
        client_socket.sendall(request.encode())
        # Recebe a resposta
        response = client_socket.recv(4096).decode()

    # Incrementa o total de requisições
    total_requests += 1
    # Extrai o status da resposta
    status = response.split(' ')[1]
    # Imprime o status da requisição
    print(f"Request to {path} received status: {status}")

# Lista de caminhos a serem testados
paths = ['/', '/index.html', '/index', '/nonexistent.html']
threads = []

# Cria threads para cada combinação de cliente e caminho
for client_id in range(num_clients):
    for path in paths:
        thread = Thread(target=send_request_and_get_response, args=(path,))
        threads.append(thread)
        thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

# Imprime o número total de requisições realizadas
print(f"Total number of requests: {total_requests}")