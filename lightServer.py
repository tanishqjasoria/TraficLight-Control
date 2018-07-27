
# coding: utf-8

# In[178]:


import numpy as np
import socket
import time
import random
timeCongest = [10,20,30]


# In[179]:


def initSocket():
    host = "127.0.0.1"
    port = 5002
    mySocket = socket.socket()
    mySocket.bind((host,port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    data = "assd"
    print ("Connection from: " + str(addr))
def sendData(data):
    print ("sending: " + str(data))
    time.sleep(1)
    conn.send(data.encode())


# In[180]:


def findDir(congestMat):
    dirMat = np.zeros(congestMat.shape + (3,))
    timeMat = np.zeros(congestMat.shape)
    #dirMat = congestMat[:][:]
    for i in range(len(congestMat)):
        for j in range(len(congestMat[i])):
            if (congestMat[i][j])==3:
                timeMat[i][j]=timeCongest[2]
            elif congestMat[i][j]==2:
                timeMat[i][j]=timeCongest[1]
            elif congestMat[i][j]==1:
                timeMat[i][j]=timeCongest[0]
    return timeMat
def Emergency(congestMat, route):
    for i in range(len(route)-2):
        s = " ".join(route)
        sendData('E')
        sendData(s)
    return dirMat


# In[181]:

cong=[]
#a=np.array([[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1],[2,0,1,0,1,3,0,2,1,0,3,1,2,0,0,1]])
for i in range(2*4*(4-1)):   
    cong.append(random.randint(1,3))

a=np.full((16,16),0,dtype=int)
for i in range(16):
    for j in range(i,16):
      if j==i+4 and i<12:
        a[i][j]=a[j][i]=cong[i+12]
      elif j==i+1 and i%4!=3:
        a[i][j]=a[j][i]=cong[(i-(i//4))]
print(a)

# In[186]:


host = "127.0.0.1"
port = 5006
mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
conn, addr = mySocket.accept()
data = "assd"
print ("Connection from: " + str(addr))
speed = findDir(a)[2][1]




while 1:
    data = str(findDir(a)[2][1])
    print ("sending: " + str(data))
    time.sleep(1)
    conn.send(data.encode())
conn.close()

