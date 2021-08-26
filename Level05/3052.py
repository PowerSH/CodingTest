value = list()

for idx in range(10):
    value.append(int(input())%42)

value = set(value)

print(len(value))