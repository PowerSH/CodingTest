def solution(phone_book):
    answer = True

    hash = {}

    for idx in phone_book:
        hash[idx] = 1
    print(hash)

    for idx1 in phone_book:
        temp = ''
        for idx2 in idx1:
            temp += idx2
            if temp in hash and temp != idx1:
                print(temp, idx1)
                answer = False    
                    
    return answer

phone_book = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]]

for idx in phone_book:
    print("Final Answer : ", solution(idx))