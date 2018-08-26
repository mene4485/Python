# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode(),end='')

# mysock.close()

import urllib.request, urllib.parse, urllib.error 


fh = urllib.request.urlopen(input("Enter a file -- "))

for line in fh:
	try:
		print(line.decode()) 
	except :
		pass