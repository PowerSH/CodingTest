import sys

T = int(sys.stdin.readline())

for idx in range(T):
    A, B = sys.stdin.readline().split()    
    
    sys.stdout.write(str(int(A) + int(B)) + '\n')