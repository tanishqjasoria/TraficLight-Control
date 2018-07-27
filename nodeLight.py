
# coding: utf-8

# In[22]:


import socket
host = "127.0.0.1"
port = 5006
nodeId =4
mySocket = socket.socket()
mySocket.connect((host,port))
message = "<"
while True:
        data = mySocket.recv(1024).decode()
#        if data=='E':
 #           data=mySocket.recv(1024).decode()
  #          c = data.split(" ")
   #         if nodeId in c:
    #            q = c.index(nodeId)
        print(data +" ")
mySocket.close()

