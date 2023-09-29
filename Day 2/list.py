#create an dynamic array 1d it should contains number b/n 20 to 30, in that
#extract and print even numbers and 2 power values
x,y =map(int, input("Enter the range").split(','))
n=int(input("Enter the size"))
l1=[]
k=0
while(n>k):
    z=int(input("Enter the value for list"))
    if z in range(x,y+1):
        l1.append(z)
        k+=1
    else:
        print("number out of range enter next value")
print(l1)
l2=[]
for i in l1:
    if(i%2==0):
        l2.append(i)
l3=[]
for i in l1:
    s=i
    for j in range(i,0,-1):
        i=i/2
        if(i==1):
            l3.append(s)
print(l3)
print(l2)