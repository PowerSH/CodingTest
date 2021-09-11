N = int(input())
T = list(map(int, input().split()))
count = 0

def isPrime(num):
    n = 2
    if num < 2:
        return False

    while n*n <= num:
        if num % n == 0: return False
        n += 1

    return True

for idx in T:
    if isPrime(idx):
        count += 1

print(count)