from socket import socket
import os

sockfd = socket()
sockfd.bind(('127.0.0.1',8031))
sockfd.listen(10)
while True:
	(new_fd,from_port) = sockfd.accept()
	print "incoming connection"
	if os.fork() == 0:
		socket.close(sockfd)
		numbytes = new_fd.recv(300)
		print numbytes
		numbytes = numbytes[:100].split()
		print numbytes
		if numbytes[1] == "/":
			req_file = "/index.html"
		else:
			req_file = numbytes[1]
		fd = open(os.getcwd()+req_file)
		data = fd .read()
		s = "HTTP/1.1 200 OK\nContent-length: %d\nContent-Type: %s\n\n%s" % (len(data),"text/html",data)
		new_fd.send(s)
		new_fd.close()
		exit(0)
	socket.close(new_fd)

