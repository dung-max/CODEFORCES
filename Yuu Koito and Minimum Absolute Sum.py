def sol():
    n = int(input())  
    a = list(map(int, input().split()))  

 
    if a[0] == -1 and a[n-1] == -1:
        a[0] = 0
        a[n-1] = 0
    elif a[0] == -1:
        a[0] = a[n-1]
    elif a[n-1] == -1:
        a[n-1] = a[0]
    
    for i in range(n):
        if a[i] == -1:
            a[i] = 0
    
    print(abs(a[0] - a[n-1]))
    
    print(*a)

t = int(input())
for _ in range(t):
    sol()
