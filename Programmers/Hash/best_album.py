import collections
# https://bomoto.tistory.com/75
def solution(genres, plays):
    answer = []

    hash_genre = collections.defaultdict(int)
    hash_play = collections.defaultdict(list)    

    for idx, genre, play in zip(range(len(genres)), genres, plays):        
        hash_genre[genre] += play
        hash_play[genre].append([idx, play])

    sorted_genre = sorted(hash_genre.items(), key=lambda x: x[1], reverse=True)    

    for key, value in sorted_genre:
        sorted_play = sorted(hash_play[key], key=lambda x: x[1], reverse=True)

        for idx, play in sorted_play[:2]:
            answer.append(idx)

    print(answer)

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays = [400, 600, 150, 2500, 500, 500]

solution(genres, plays)