X = int(input())

# n*(n+1)/2 = X
# n*(n+1)   = 2*X
# n^2 - (n+1) = 2*X

n = 0
sum = 0

while n*(n+1) < 2 * X:
    n += 1
    sum += n
    
    print(n)
    
print(sum)

# if n%2 == 0:
