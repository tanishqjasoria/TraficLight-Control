
def count_car(file):
	wordcount=0
	lst=[]
	flag=0
	for word in file.read().split():
		if flag==1:
			lst.append(word)
			flag=0
		if word in {'car'}:
			wordcount+=1
			flag=1
	return wordcount,lst

def count_truck(file):
	wordcount=0
	lst=[]
	flag=0
	for word in file.read().split():
		if flag==1:
			lst.append(word)
			flag=0
		if word in {'truck'}:
			wordcount+=1
			flag=1
	return wordcount,lst

def count_motorcycle(file):
	wordcount=0
	lst=[]
	flag=0
	for word in file.read().split():
		if flag==1:
			lst.append(word)
			flag=0
		if word in {'bike'}:
			wordcount+=1
			flag=1
	return wordcount,lst

#file=open("total.txt","r+")
#print count_truck(file)
#print count_car(file)
#file.close()

