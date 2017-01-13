#12/15/2016
#Xiaozheng(Will) Guo
#Python socket proxy server

from socket import *
import sys
import requests
import os

if len(sys.argv) <= 1:
    print '''Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server'''

    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerPort = 8887
tcpSerSock = socket(AF_INET, SOCK_STREAM)
serverip = sys.argv[1]
print 'serverip = [[ ' + serverip + ' ]]'
tcpSerSock.bind((serverip, tcpSerPort))
tcpSerSock.listen(20)

while 1:
    # Strat receiving data from the client 
    print 'Ready to serve...'

    tcpCliSock, addr = tcpSerSock.accept() 
    print 'Received a connection from: [[ ', addr, ' ]]' 

    
    message = tcpCliSock.recv(1024)
    
    print 'message = ***********\n\n' + message + '\n******************'
    # Extract the filename from the given message 

    if message.strip() == '':
        continue;
    print 'message.split()[1] = [[ ' + message.split()[1] + ' ]]'

    # if no specific file, use index
    filename = message.split()[1].partition("/")[2].partition('/')[2]
    print 'filename = [[ ' + filename + ' ]]'

    filename2 = filename
    if (filename.partition('/')[2].strip() == ''):
        filename2 = filename + 'index'
    print 'filename2 = [[ ' + filename2 + ' ]]'

    fileExist = "false"

    filetouse = "/" + filename2
    print 'filetouse = [[ ' + filetouse + ' ]]'

    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")

        
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
            print '**************Read from cache*****************'

    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            
              
            c = socket(AF_INET, SOCK_STREAM)
            
# now we deal with hostname
            
            hostn2 = filename.partition('/')[0]


            # hostn = filename.replace("www.","",1) 
            print 'hostn2 = [[ ' + hostn2 + ' ]]'
            

            try:
                # Connect to the socket to port 80
                
                
                c.connect((hostn2, 80))
                                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('r', 0)

                getFile = '/' + filename.split('/', 1)[1]
                
                getMessage = "GET " + getFile + " HTTP/1.0\n\n"
                print 'getMessage = [[ ' + getMessage + ' ]]'

                fileobj.write(getMessage)

                

                # Read the response into buffer
                
                
                buffer = fileobj.readlines()
                               
                # Create a new file in the cache for the requested file. 
                # Also send the response in the buffer to client socket
                # and the corresponding file in the cache
                noPathName = filename2.split('/')[-1]
                pathList = filename2.split('/')[:-1]
                path = '/'.join(pathList)

                # we use exception here because we might write in one file twice
                # then makedirs will throw a OSError exception
                try:

                    os.makedirs(path)
                except OSError:
                    pass

                # exception here because we might need to create a file with 
                # very long filename which open function cannot handle, so we
                # choose to pass in this situation
                try:

                    tmpFile = open("./" + filename2,"wb")
                except IOError:
                    pass


                
                for i in buffer:
                    tmpFile.write(i)
                    tcpCliSock.send(i)
                            
            except :
                print "Illegal request"
        else:
            # HTTP response message for file not found
            
            
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n")
            tcpCliSock.send("Content-Type:text/html\r\n")
               
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
sys.exit()
