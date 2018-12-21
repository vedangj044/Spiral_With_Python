l = []
n = int(input())
if n%2==0:
    print("enter odd number")

for i in range(n):
    a=[]
    for i in range(n):
        a.append(1)
    l.append(a)
l[n//2][n//2+1]=2

def nine(b):
    p = b//2
    c = (b-2)*(b-2)+1
    for i in range(b-1):
        l[n//2-p+1+i][n//2+p] = c+i
        l[n//2+p][n//2+p-i] = c+b-2+i
        l[n//2+p-i][n//2-p] = c+2*b-3+i
    for i in range(b):
        l[n//2-p][n//2-p+i] = c+3*b-4+i

i=3
while n+2!=i:
    nine(i)
    i=i+2

for i in l:
    print(i)
