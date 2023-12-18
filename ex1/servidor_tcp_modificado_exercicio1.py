
import socket 

def main():
    # Criação do socket TCP
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Realização do bind do processo na porta 2023
    socketTCP.bind(("127.0.0.1", 2023))
    socketTCP.listen()
    print("Servidor TCP está esperando conexões!")

    while True:
        # Bloqueio da thread principal - esperando novas conexões
        socketCliente, endereco = socketTCP.accept()
        print(f"Endereço do Cliente: {endereco}")

        while True:
            # Conexão feita, esperando requisição do cliente
            msg = socketCliente.recv(1024)
            if not msg:
                break  # Se nenhuma mensagem for recebida, sair do loop interno

            # Mensagem chegou! Vamos imprimi-la na tela!
            print(msg.decode())

            # Enviando resposta para o cliente 
            socketCliente.sendall(str.encode("Resposta do servidor!"))

        # Fechando a conexão com o cliente
        socketCliente.close()
        print(f"Conexão com {endereco} encerrada")

if __name__ == "__main__":
    main()
