text = input()

dial = [' ', ' ', ' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

for idx1 in range(len(text)):
    for idx2 in range(len(dial)):
        if text[idx1] in dial[idx2]:            
            sum += idx2

print(sum)