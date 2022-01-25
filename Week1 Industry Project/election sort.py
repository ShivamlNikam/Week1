
import time
from random import randint

X = [ ]
print("SHIVAM NIKAM A2 043")
n = int(input("Enter number of elements: "))
a = int(input("Enter the minimum range: "))
b = int(input("Enter the maximum range: "))
for i in range(0, n):
    x = randint(a, b)
    X.append(x)

t1 = time.time()

for i in range(len(X)):
    sindex = i
    for j in range(i+1, len(X)):
        if(X[sindex]>X[j]):
            sindex = j
    X[i],X[sindex] = X[sindex], X[i]
t2 = time.time()


print("Time taken : ", (t2-t1)*1000)
#print("Sorted List : ")
#for i in range(len(ToSort)):
#    print(ToSort[i])