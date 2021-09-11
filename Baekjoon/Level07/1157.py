text = input()
Count = [chr(65+x) for x in range(26)]
count = [chr(97+x) for x in range(26)]
cnt = [0 for x in range(26)]

num = 0

for idx in range(len(text)):
    if text[idx] in count:
        cnt[count.index(text[idx])] += 1        

    if text[idx] in Count:
        cnt[Count.index(text[idx])] += 1        

if cnt.count(max(cnt)) != 1:
    print("?")
else:
    print(Count[cnt.index(max(cnt))])
