import time
from random import randint

sortedArray =[]
print("SHIVAM NIKAM A2 034")
n=int(input("Enter the number of input:"))
a=int(input("Enter the lower bound:"))
b=int(input("Enter the upper bound:"))

#unsorted array
for i in range(n):
    randomNumber = randint(a,b)
    sortedArray.append(randomNumber)

t1 = time.time()

for i in range(1,n):
    key=sortedArray[i]

    j=i-1

    while j>=0 and key<sortedArray[j]:
        sortedArray[j+1]=sortedArray[j]
        j-=1
    sortedArray[j+1]=key

t2=time.time()


print("Time Complexity :",(t2-t1)*1000)