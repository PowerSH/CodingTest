from itertools import permutations
import math

def solution(numbers):
    answer = 0
    number_set = []
    numbers_set = []

    for idx in numbers:
        number_set.append(idx)
        if int(idx) > 1:
            numbers_set.append(idx)    
    
    print(number_set)
    for idx in range(2, len(number_set)+1):
        numbers_set += list(map(''.join, permutations(number_set, idx)))
        numbers_set = list(set(list(map(int, numbers_set))))

    print(numbers_set)

    def check_pnum(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False

        return True

    for idx in numbers_set:
        print("Debug:",idx)
        if check_pnum(idx):
            print("This is Pnum : ", idx)
            answer += 1

    return answer


numbers = "123"
print(solution(numbers))