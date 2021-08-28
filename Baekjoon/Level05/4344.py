C = int(input())

for idx in range(C):
    student = list(map(int, input().split()))
    stu_score = student[1:]
    stu_count = student[0]
    
    over_avg = sum(stu_score)/stu_count

    over_avg_list = list(filter(lambda x: x > over_avg, stu_score))

    print("{:.3f}%".format(((len(over_avg_list)/stu_count) * 100)))