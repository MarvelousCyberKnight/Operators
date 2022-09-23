n=int(input())
sum=0
while(n>0):
    sum=sum+(n%10)
    n=n//10
c=int(sum//10)
d=sum%10
print(c+d)
