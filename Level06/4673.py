N = 10000
remover = list(x for x in range(N))

def d(n):    
    Dn = n
    while(n > 0):
        Dn += (n%10)
        n //= 10
    if Dn < 10000:
        return Dn
    else:
        return 0

for idx in range(N):    
    if d(idx) in remover:
        remover.remove(d(idx))

for idx in range(len(remover)):    
    print(remover[idx])