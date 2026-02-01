import sys
# 문자열
# 가장 많이 존재하는 알파벳 대문자로 출력하기
# set으로 문자 뽑아내고 count로 개수 세기

input = sys.stdin.readline

word = input().strip().upper()

# 2. 중복을 제거한 문자 리스트 생성 (예: MISSISSIPI -> ['M', 'I', 'S', 'P'])
unique_words = list(set(word))

cnt_list = []

# 각 문자가 원본에 몇개 등장했는지 카운트
for x in unique_words:
    cnt = word.count(x) # 원본 문자열에서 카운트 함
    cnt_list.append(cnt)

# 가장 많이 사용된 것
if cnt_list.count(max(cnt_list)) > 1: # 최댓값이 2개 이상
    print('?')
else:
    # 최댓값의 인덱스를 찾아 그 위치의 알파벳 출력
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])