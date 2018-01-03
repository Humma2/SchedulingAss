pro=[]
total=int(raw_input("Enter Count:"))
index=0
bt=0
for index in xrange(total):
	pro.append([])
	pro[index].append(raw_input("Enter P.Name:"))
	pro[index].append(int(raw_input("A.T:")))
	pro[index].append(int(raw_input("B.T:")))
	bt=bt+pro[index][2]
	pro.sort(key=lambda pro:pro[1])

index=0
print "Process,Arrival time,Burst Time"
for index in xrange(total-1):
	print pro[index]

print "Total Busrt Time :" ,bt

