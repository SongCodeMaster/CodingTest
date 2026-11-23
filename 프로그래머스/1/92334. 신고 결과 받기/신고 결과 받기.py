# 신고 처리 결과 받은 메일을 사용자마다 return해라. 
# id_list는 딕셔너리로 보관, report로 딕셔너리 값 증가시키기
# 특정조건 넘은사람은 result 배열 개수 채우기
def solution(id_list, report, k):
    answer = []
    report = set(report)
    
    # 당한애들 딕셔너리
    reported_dict = {i : 0 for i in id_list}

    # 신고한애들 딕셔너리
    reporting_dict = {i : 0 for i in id_list}
    # 당한애들 기록
    for u in report:
        reporting, reported = u.split(" ")
        reported_dict[reported] += 1
        reporting_dict
        
    for v in report:
        reporting, reported = v.split(" ")
        if reported_dict[reported] >= k:
            reporting_dict[reporting] += 1
    
    for i in reporting_dict:
        answer.append(reporting_dict[i])
    
    return answer