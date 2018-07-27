import numpy as np 
import cv2
import random
import math
import time



def display_lights(total_nodes,c,it_time):
	img=np.zeros((768,1024,3),np.uint8)						#Starting the image file
	a=(range(1,5,1))										#a is the total number of lights
	b=(range(1,total_nodes+1,1))
	trfc=np.full((total_nodes,4),0,dtype=int)
	for i in range(16):
		if i-4>=0:
			trfc[i][0]=c[i][i-4]
		if i+4<=total_nodes-1:
			trfc[i][3]=c[i][i+4]
		if i+1<=total_nodes-1:
			trfc[i][2]=c[i][i+1]
		if i-1>=0:
			trfc[i][1]=c[i][i-1]
	on_time=np.full((total_nodes,4),0,dtype=float)
	on_time[:]=trfc
	#print on_time
	for j in b:
		sum_=np.sum(on_time[j-1],axis=0)
		on_time[j-1]=(on_time[j-1]*it_time)/sum_
	print on_time
	#print trfc

	#print trfc
	#print b*(1024/(total_nodes+1))
	start_time=time.time()
	while(1):
		curr_time=time.time()-start_time
		for j in b:
			sum_time=0
			for i in a:
				if trfc[j-1][i-1]!=0:
					if sum_time<curr_time<sum_time+on_time[j-1][i-1]:
						#if trfc[j-1][i-1]==1:
						cv2.circle(img,(i*(1024/5),(j*(768/(total_nodes+1)))),768/((total_nodes+1)*2),(0,255,0),-1)
						#if trfc[j-1][i-1]==3:
							#cv2.circle(img,(i*(1024/5),(j*(768/(total_nodes+1)))),768/((total_nodes+1)*2),(0,0,255),-1)
						#if trfc[j-1][i-1]==2:
							#cv2.circle(img,(i*(1024/5),(j*(768/(total_nodes+1)))),768/((total_nodes+1)*2),(0,255,255),-1)
					else:
						cv2.circle(img,(i*(1024/5),(j*(768/(total_nodes+1)))),768/((total_nodes+1)*2),(0,0,255),-1)	
					sum_time=sum_time+on_time[j-1][i-1]
			#print sum_time		

		if curr_time>it_time:
			break
		#print curr_time
		cv2.imshow("Ouput",img)
		cv2.waitKey(10)

# while(1):
# 	cong=[]
# 	total_nodes=16
# 	sqr=math.sqrt(total_nodes)
# 	sqr=int(sqr)

# 	for i in range(2*sqr*(sqr-1)):
# 	    cong.append(random.randint(1,3))
	  
# 	#print "\n",cong[5]

# 	c=np.full((total_nodes,total_nodes),0,dtype=int)
# 	for i in range(total_nodes):
# 		for j in range(i,total_nodes):
# 		  if j==i+4 and i<12:
# 		    c[i][j]=c[j][i]=cong[i+12]
# 		  elif j==i+1 and i%4!=3:
# 		    c[i][j]=c[j][i]=cong[(i-(i//sqr))]
# 	#print c,"\n"

# 	display_lights(total_nodes,c,20)