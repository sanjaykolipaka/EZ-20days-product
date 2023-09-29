n = int(input())
s =0
s1 = 0
while n:
    rem = n%10
    s =s+rem
    n = n//10
print(s)

n1 = int(input())
n2 = str(n1)
for i in range (1,n,n//10):
    s1 = s1 + i
print(s1)
