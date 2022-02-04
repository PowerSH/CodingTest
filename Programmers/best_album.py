def solution(genres, plays):
    hash = {}
    counter = 0

    for idx in genres:
        if idx in hash:
            hash[idx] += plays[counter]
        else:
            hash[idx] = plays[counter]

        counter += 1

    print("Current Hash : ", hash)    



    answer = []
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)