import socket 

# criação do socket TCP
socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# realização do bind do processo na porta 2023
socketTCP.bind(("127.0.0.1", 2023))
socketTCP.listen()
print("Servidor TCP está esperando conexões!")

# bloqueio da thread principal - esperando novas conexões
socketCliente, endereco = socketTCP.accept()
print(f"Endereço do Cliente: {endereco}")

# conexão feita, esperando requisição do cliente
msg = socketCliente.recv(1024)

# Mensagem chegou! Vamos imprimi-la na tela!
print(msg)


# enviando resposta para o cliente 
socketCliente.sendall(str.encode("Resposta do servidor!"))
socketCliente.close()