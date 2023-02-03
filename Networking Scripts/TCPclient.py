import socket

target_host = "kyautomotive.kimworks.buzz"
target_port = 80

#creation of a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting the client

client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: kyautomotive.kimworks.buzz\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode())
client.close()