import socket 

ip = '127.0.0.1' 
port = 50000 


addr = (ip,port) 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 

mensagem = input("digite uma mensagem para enviar ao servidor\n") 

client_socket.sendall(str.encode(mensagem)) 

print('mensagem enviada') 

data = client_socket.recv(1024)

print('Mensagem ecoada:', data.decode())
