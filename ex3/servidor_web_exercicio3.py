import socket
from threading import Thread

# Função para processar a conexão com cada cliente
def process_client_connection(client_socket, client_address):
    try:
        # Recebe a requisição do cliente e decodifica
        request = client_socket.recv(1024).decode()

        # Imprime a requisição recebida para fins de depuração
        print(f"Request from {client_address}: {request}")

        # Extrai o método HTTP, o caminho e o restante da requisição
        http_method, path, _ = request.split(' ', 2)

        # Verifica o caminho da requisição e define o arquivo correspondente
        if path in ['/', '/index.html', '/index']:
            file_path = "index.html"
        else:
            file_path = "404.html"

        # Tenta abrir e ler o arquivo
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Cria a resposta HTTP baseada no arquivo lido
                response = (f'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n{content}' 
                            if '404' not in file_path 
                            else f'HTTP/1.1 404 NOT FOUND\nContent-Type: text/html; charset=utf-8\n\n{content}')
        except FileNotFoundError:
            # Caso o arquivo não seja encontrado, retorna erro 500
            response = 'HTTP/1.1 500 Internal Server Error\n\nInternal Server Error'

        # Envia a resposta para o cliente
        client_socket.sendall(response.encode())
    finally:
        # Fecha a conexão com o cliente
        client_socket.close()

# Função para iniciar o servidor web
def start_web_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2023
    # Associa o socket à porta 2023
    server_socket.bind(('127.0.0.1', port))
    # Coloca o servidor para escutar por conexões
    server_socket.listen()
    # Imprime uma mensagem indicando que o servidor está rodando
    print(f"Servidor rodando na porta: {port}")

    # Loop infinito para aceitar conexões
    while True:
        # Aceita uma conexão do cliente
        client_socket, client_address = server_socket.accept()
        # Cria uma nova thread para lidar com a conexão do cliente
        Thread(target=process_client_connection, args=(client_socket, client_address)).start()

# Verifica se o módulo é o principal e inicia o servidor
if __name__ == '__main__':
    start_web_server()