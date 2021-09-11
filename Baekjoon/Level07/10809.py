S = input()
alphabet = [chr(97+x) for x in range(26)]
order = [-1 for x in range(26)]
cnt = -1

for idx in range(len(S)):
    cnt += 1

    if order[alphabet.index(S[idx])] == -1:
        order[alphabet.index(S[idx])] = cnt

for _, idx in enumerate(order):
    print(idx, end=' ')