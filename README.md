Documentação socket de rede TCP


************* COMO USAR ******************

Para usar esses sockets é bem simples primeiro execute o socket:

- servidor_Socke.py

para o servidor ficar escutando, ou seja, esperando que o cliente estabeleça a comunicação

depois execute o socket:

 - cliente_socke.py

e envie sua mensagem

Para executar esses programas pelo terminal é simples, basta usar os comandos:

Para o servidor_Socke.py

chmod 744 servidor_Socke.py   # para dá permissão
./servidor_Socke.py           # para executar

Para o cliente_socke.py

chmod 744 cliente_socke.py   # para dá permissão
./cliente_socke.py           # para executar


Funcionamento do software

 - Primeiro, o servidor precisa criar um socket especificando qual o tipo de endereço(IPV4/IPV6) será usado e o tipo de socket (TCP/UDP)
   serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 - Após o passo anterior, é preciso vinculado o IP com uma porta, esse processo é feito atráves do método bind
   serv_socket.bind(addr)

 - Depois, o servidor deve entrar no modo de escuta, ou seja, espera que um cliente inicie a comunicação
   serv_socket.listen(3)

 - O servidor também deve aceitar a comunicação quando ela for feita
   conn, cliente = serv_socket.accept()

 - O cliente também irá criar um socket
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 - E irá solicitar a conexão com o servidor
   client_socket.connect_ex(addr)

 - Cliente envia dados
   client_socket.sendall(str.encode(mensagem))

 - Servidor lê os bytes até um tamanho definido
   data = conn.recv(1024)

 - Devolve dados para o cliente
   conn.sendall(data)

 - O cliente Lê os bytes até um tamanho definido
   data = client_socket.recv(1024)

 - Servidor termina a conexão
   conn.close()


Propósito do software, motivação da escolha do protocolo de transporte e os requisitos mínimos de funcionamento

Os Sockets são empregados para o envio de mensagens através de uma rede. São uma das formas mais comum de IPC -Inter-Process Communication.As aplicações mais comuns para sockets são aplicações cliente-servidor, nas quais um servidor espera por conexões de clientes. Nesse caso, será  criado um socket tcp, pois com o socket tcp os dados são enviados sem erros ou duplicação, e recebidos na mesma ordem em que foram enviados.
Para que a comunicação aconteça, é necessário ter um serviço com o papel de servidor e outro com o papel do cliente. O servidor deve ficar ouvindo, ou seja, no estado de aguardo por alguma solicitação de clientes que desejam se comunicar. E o cliente será o responsável por iniciar a comunicação com o servidor. Dessa forma, é possível notar que um dos requisitos mínimos para estabelecer uma comunicação é ter um servidor, esperando por uma solicitação de comunicação e um cliente para iniciar a comunicação.


Protocolo da camada de aplicação HTTP

O HTTP - protocolo de transferência de hipertexto é um protocolo da camada de aplicação, responsável pela transmissão de documentos de hipermídia, como o HTML. Sempre que você abre o seu navegador e digita o endereço de alguma página Web, por exemplo: (wwww.google.com.br), um Socket é criado pelo navegador. Neste caso, você é o Cliente e o computador em que a página Web está armazenada é o Servidor. Nesse contexto, o usuário final (você) não tem ciência de um conjunto de etapas que ocorre internamente dentro do sistema operacional (Windows/Linux/Mac) do Servidor e do Cliente.  No nível da camada de aplicação, geralmente o navegador faz uma comunicação usando o protocolo HTTP ou HTTPS. Estes permitem a obtenção de recursos, tais como documentos HTML que são a base de toda página Web. Neste ponto, é importante dizer que cada protocolo da camada de aplicação tem associado a ele uma porta padrão de operação, no caso do protocolo HTTP a porta 80 é o padrão universal, no HTTPS temos a porta 443, o FTP tem a porta 23, etc. Na sequência (Camada de Transporte), escolhe-se como a comunicação irá tratar a entrega de dados. Neste caso, se usar TCP temos a garantia de que nenhuma parte dos dados transmitidos serão perdidos.
