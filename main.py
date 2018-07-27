import pylab as plt
#import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import cv2
import count as ct
import Traffic as tf
import setparam as sp
import math
import random
import traffic_signl as ts
import configparser
#Congfigratuion file reader, donot edit anything in this code
def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

config = configparser.ConfigParser()
config.read('config/config.ini')

total_nodes=int(ConfigSectionMap("Node")['number'])
sqr=math.sqrt(total_nodes)
sqr=int(sqr)
src=int(ConfigSectionMap("Node")['src'])
des=int(ConfigSectionMap("Node")['des'])
rang=int(ConfigSectionMap("Fuzzy")['range'])
lanes=int(ConfigSectionMap("Fuzzy")['lanes'])
tym=int(ConfigSectionMap("Traffic")['time'])
'''
a=np.matrix([[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0],
            [0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0],
            [0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0],
            [0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0],
            [0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0],
            [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0]])
'''
dist=[1.19,1.20,1.30,1.24,1.31,1.26,1.13,1.25,1.28,1.16,1.16,1.14,1.38,1.26,1.28,0.73,0.66,0.58,0.72,0.69,0.62,0.62,0.67,0.72,0.72,0.68,0.75,0.61,0.74,0.62,0.78]
i,j=0,0
a=np.full((total_nodes,total_nodes),0,dtype=float)#Dont edit this
for i in range(total_nodes):#Dont Edit this
  for j in range(i,total_nodes):
    if j==i+4 and i<12:
      a[i][j]=a[j][i]=dist[i+12]
    elif j==i+1 and i%4!=3:
      a[i][j]=a[j][i]=dist[i-(i%sqr)]
#print a
lis=[]

for i in range(2*sqr*(sqr-1)):
  if i%3==0:
    Obj=sp.Path(rang,lanes)
    lis.append(Obj)
  if i%3==1:
    Obj=sp.Path(rang,lanes)
    lis.append(Obj)
  if i%3==2:
    Obj=sp.Path(rang,lanes)
    lis.append(Obj)
d=1



while(1):

  l=d%3+1

  file=open("total.txt","r")#dont change

  cong=[]

  cc,ls1=ct.count_car(file)#Dont change from here
  file=open("total.txt","r")
  tc,ls2=ct.count_truck(file)
  file=open("total.txt","r")
  mc,ls3=ct.count_motorcycle(file)#Till here

  #print cc,tc,mc,ls1,ls2,ls3

  for i in range(2*sqr*(sqr-1)):#Randomisation algorithm
    if i==5:
      tf.fuzzy(cc,ls1, tc, ls2,mc,ls3,lis[i])
      cong.append(lis[i].congestion)#Actual feed
    else:
      cong.append(random.randint(1,3))
  
  print "\n",cong[5]#Print the congesrion list

  c=np.full((total_nodes,total_nodes),0,dtype=int)#Congestion matrix building starts
  for i in range(total_nodes):
    for j in range(i,total_nodes):
      if j==i+4 and i<12:
        c[i][j]=c[j][i]=cong[i+12]
      elif j==i+1 and i%4!=3:
        c[i][j]=c[j][i]=cong[(i-(i//sqr))]
  print c,"\n"                                    #Ends

  e=np.multiply(a,c)
  #print e,"\n"
  #print(c.item(0,0))
  #print(c.shape)
  g=nx.Graph()                                    #Graph building starts
  for i in range(total_nodes):
      for j in range(total_nodes):
          if (c.item(i,j) ==1) :
              g.add_edge(i,j,color='g',weight=e.item(i,j),length=100)

          if (c.item(i,j) ==2) :
              g.add_edge(i,j,color='y',weight=e.item(i,j),length=100)

          if (c.item(i,j) ==3) :
              g.add_edge(i,j,color='r',weight=e.item(i,j),length=100)
  #print(g[0][4])
  fixed_pos={0:(0,6),1:(2,6),2:(4,6),3:(6,6),4:(0,4),5:(2,4),6:(4,4),7:(6,4),8:(0,2),9:(2,2),10:(4,2),11:(6,2),12:(0,0),13:(2,0),14:(4,0),15:(6,0)}
  fixed_nodes =fixed_pos.keys()#dont change
  pos=nx.spring_layout(g,pos=fixed_pos,fixed=fixed_nodes)#dont change
  edges=g.edges()

  colors = [g[u][v]['color'] for u,v in edges]
  weights = [g[u][v]['weight'] for u,v in edges]
  
  nx.draw(g, pos, edges=edges, edge_color=colors, width=15, with_labels=True,node_size=2000)
                                                  #Graph building ends
  path = nx.shortest_path(g,source=src,target=des,weight="weight")#dont changne
  src=path[1]                                     #Updating path
  if src==des:
    src=random.randint(1,14)
  print path, nx.shortest_path_length(g,source=src,target=des,weight="weight")
  path_edges = list(zip(path,path[1:]))
  nx.draw_networkx_nodes(g,pos,nodelist=path)
  nx.draw_networkx_edges(g,pos,edgelist=path_edges,edge_color='black',width=4,arrows=True,style='dashdot')
  #lightTime = findDir(c)
  plt.axis('equal')
  plt.ion()
  plt.savefig("Graph.png", dpi=None, bbox_inches='tight')
  plt.draw()
  plt.show()
  ts.display_lights(total_nodes,c,tym)
  plt.pause(0.1)
  plt.clf()
  file.close
  d+=1

  #img=cv2.imread("Graph.png")
  #cv2.imshow("output",img)
