def Fibonacci_by_loop(n):
    p1=0
    p2=1
    while p1<n:
        print(p2)        
        sum=p1+p2
        
        p1=p2
        p2=sum
        
print(Fibonacci_by_loop(5))

# 0 ,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
