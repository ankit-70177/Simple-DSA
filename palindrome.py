# Your code here
l=int(input())
r=int(input())

for i in range(l,r+1):
    d=0
    n=i
    
    while n>0:
        ld = n%10
        d=(d*10)+ld
        n//=10
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if d==i and is_prime==True and i!=1:
        print(i,end=" ")
