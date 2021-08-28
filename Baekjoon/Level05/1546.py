N = int(input())

score = list(map(int, input().split()))

max_value = max(score)

print((sum(score)/max_value) / N * 100)