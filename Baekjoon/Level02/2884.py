H, M = input().split()
H, M = int(H), int(M)

if M-45 >= 0:
    M = M-45
else:
    M = M+15
    H = (H-1)%24
        
print(H, M)