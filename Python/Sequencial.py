import time
start=time.time()
students=[1,2,3,4]
recieved=['F','F','F','F']

for i in range(len(students)):
    recieved[i]='T'
for j in range(len(students)):
    print(recieved[j])

print("\nTime taken is %s " % (time.time()-start))

