# def, play 시간동안 겹치는 시간이 있는지 (시간 사이에 들어오는지 방문해보기 )
# def, 겹치는 시간대 누적시간 합하기
# 최대 누적시간 계산하여 시작시간 return 하기?

def sec_to_time(time_int):
    h = time_int // 3600
    m = (time_int % 3600) // 60
    s = time_int % 60
    
    return f"{h:02d}:{m:02d}:{s:02d}"
# ('01:20:15')문자열 -> 초시간 int 변환하기
def time_to_sec(time_string):
    h,m,s = map(int, time_string.split(':'))
    h = 60 * 60 * h
    m = m * 60
    result = h + m + s
    return result

# 공익광고 어디에 넣을지 찾아야함.
def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    viewer = [0] * (play_sec+1)
    
    # 각 로그별로 시작지점 , 끝지점 플래그
    for log in logs:
        start_time, end_time = log.split('-')
        start = time_to_sec(start_time)
        end = time_to_sec(end_time)

        viewer[start] += 1
        viewer[end] -= 1
        
    # 시청자 수 누적합 구하기
    for i in range(1, play_sec + 1):
        viewer[i] += viewer[i-1]
        
    # 슬라이딩 윈도우 구현해서 윈도우 내부에서 가장 많은 시청자 기록된 i 초기화
    current_sum = sum(viewer[:adv_sec]) # 초기 윈도우
    max_sum = current_sum
    max_start = 0
    
    # 다음 합 = 이전합 - (빠진애) + 새로들어온애(맨뒤)
    for i in range(1, play_sec - adv_sec + 1):
        current_sum = current_sum - viewer[i-1] + viewer[i + adv_sec - 1]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = i
            
    return sec_to_time(max_start)