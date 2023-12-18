requisicao = socketCliente.recv(1024).decode()
print(requisicao)
resposta = 'HTTP/1.0 200 OK\n\n<h1>Hello World</h1>'
socketCliente.sendall(resposta.encode())
socketCliente.close()