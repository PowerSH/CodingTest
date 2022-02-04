def solution(clothes):
    hash = {}

    counter = 0
    temp = 1

    # 종류만 분류하자
    for idx1 in clothes:
        if idx1[1] in hash:            
            hash[idx1[1]] += 1            
        else:
            hash[idx1[1]] = 1            
    
    # 경우의 수를 구하자
    for idx in hash:        
        temp *= (hash[idx]+1)

    answer = counter + temp - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))