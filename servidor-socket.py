import socket 

host = 'localhost'    
port = 50000  

addr = (host, port) 

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.bind(addr) 
serv_socket.listen(3) 

print('aguardando conexao')
 
conn, cliente = serv_socket.accept() 

print('conectado em:', cliente) 


while True:
	data = conn.recv(1024) 
	
	if not data:
		print('Fechando a conexao')
		conn.close()
		break
	print("mensagem recebida:", data)
	conn.sendall(data)
