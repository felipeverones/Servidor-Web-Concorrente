import socket

def main():
    # Criando um socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vinculando o socket a um endereço e porta
    servidor.bind(('localhost', 2023))

    # Colocando o socket em modo de escuta
    servidor.listen()
    print("Servidor HTTP escutando na porta 2023...")

    while True:
        # Aceitando uma nova conexão
        conexao, endereco = servidor.accept()
        print(f"Conectado com {endereco}")

        # Recebendo a requisição HTTP do cliente
        requisicao = conexao.recv(1024).decode()
        print(requisicao)

        # Montando a resposta HTTP
        http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<h1>Hello World</h1>"

        # Enviando a resposta para o cliente
        conexao.sendall(http_response.encode())

        # Fechando a conexão com o cliente atual
        conexao.close()
        print(f"Conexão com {endereco} fechada")

if __name__ == "__main__":
    main()
