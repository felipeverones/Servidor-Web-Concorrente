import socket 

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTCP.connect(("127.0.0.1", 2023)) #endereco ip do servidor e porta
socketTCP.sendall((b"Mensagem para o servidor!"))
msg = socketTCP.recv(1024)
print(f"Recebido {msg!r}")
socketTCP.close()