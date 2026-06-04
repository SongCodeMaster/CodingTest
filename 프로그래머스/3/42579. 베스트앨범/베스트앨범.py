from collections import defaultdict
# 장르 먼저 수록 -> 장르 내에서 많이 재생된 순서 수록
def solution(genres, plays):
    answer = []
    
    genre_total_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total_plays[genre] += play
        genre_songs[genre].append((play, i)) # 재생횟수, 고유번호
    
    # 장르별 총 재생 횟수 많은 순 정렬
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda x: genre_total_plays[x], reverse=True)
    
    # 각 장르 내에서 정렬 기준 적용
    for genre in sorted_genres:

        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        for i in range(min(len(sorted_songs), 2)):
            answer.append(sorted_songs[i][1])
    
    return answer