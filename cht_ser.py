from socket import *
fd = socket(AF_INET, SOCK_DGRAM)
fd.bind(('127.0.0.1',4000))
while 1:
	x = fd.recvfrom(100)
	print "[you]:",x[0]
	i = raw_input("[me ]:")
	fd.sendto(i,x[1])
	print x
