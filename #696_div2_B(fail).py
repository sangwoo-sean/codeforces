def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    b=1+n
    while not isPrime(b):
        b+=1
    c=b+n
    while not isPrime(c):
        c+=1
    print(b*c, b, c)