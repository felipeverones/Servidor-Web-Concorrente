
# Servidor Web Concorrente - Tutorial 2023/2

Este repositório contém um projeto prático para aprender a construir um servidor web concorrente. Este trabalho foi desenvolvido como parte da disciplina de Sistemas Operacionais na Universidade Federal de Santa Catarina, sob a orientação do Prof. Roberto Rodrigues Filho. O projeto utiliza a linguagem Python e abrange conceitos de sockets TCP e threads.

## Funcionalidades

- Implementação de um servidor web que lida com múltiplas requisições simultaneamente usando threads
- Uso de sockets TCP para comunicação de rede
- Scripts de cliente para testar a funcionalidade do servidor


# Resumo de cada exercício

## Exercício 1
Neste código, foi criado um servidor TCP simples usando o módulo socket em Python. O servidor escuta na porta 2023 e aguarda conexões de clientes. Quando um cliente se conecta, o servidor imprime o endereço do cliente e entra em um loop para receber mensagens do cliente. As mensagens recebidas são imprimidas no console, e uma resposta simples "Resposta do servidor!" é enviada de volta ao cliente. O servidor continua a aguardar mensagens do cliente até que a conexão seja encerrada.

`` Explicação linha por linha no próprio código!`` 

## Exercício 2
Neste código, foi criado um servidor HTTP básico usando o módulo socket em Python. O servidor escuta na porta 2023 e aceita conexões de clientes. Quando um cliente se conecta, o servidor lê a requisição HTTP do cliente, que deve ser uma solicitação GET. Em seguida, o servidor constrói uma resposta HTTP simples com um status 200 (OK) e uma página HTML que exibe "Hello World". A resposta é enviada de volta ao cliente, e a conexão é fechada.

`` Explicação linha por linha no próprio código!`` 


## Exercício 3

### Servidor
Neste código, foi implementado um servidor web mais completo usando o módulo socket e threads. O servidor escuta na porta 2023 e aceita conexões de clientes. Quando um cliente se conecta, uma nova thread é criada para lidar com essa conexão. O servidor lê a requisição HTTP do cliente, extrai o método HTTP e o caminho da requisição. Com base no caminho, o servidor decide qual arquivo HTML deve ser servido (por exemplo, "index.html" ou "404.html").

Se o arquivo HTML correspondente for encontrado, o servidor o lê e cria uma resposta HTTP com um status 200 (OK) ou 404 (NOT FOUND), dependendo da existência do arquivo. A resposta inclui o tipo de conteúdo (text/html) e o próprio conteúdo HTML do arquivo. A resposta é enviada de volta ao cliente, e a conexão é fechada.

`` Explicação linha por linha no próprio código!`` 


### Cliente
Neste código, foi implementado um cliente que envia solicitações HTTP GET para o servidor web criado no exercício anterior. O cliente pode enviar várias solicitações simultaneamente usando threads. Ele envia solicitações para diferentes caminhos, como "/", "/index.html", "/index" e "/nonexistent.html". O número total de requisições é contabilizado, e o status de cada resposta é impresso no console.

Isso permite simular várias solicitações simultâneas ao servidor web e verificar como ele lida com múltiplos clientes e diferentes solicitações de caminhos. O cliente é uma maneira de testar e avaliar o servidor web.

`` Explicação linha por linha no próprio código!`` 


## Contribuições

Sugestões e contribuições para melhorar o servidor web são bem-vindas. Por favor, abra um issue ou um pull request para contribuir.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).