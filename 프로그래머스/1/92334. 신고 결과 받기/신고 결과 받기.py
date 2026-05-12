def solution(id_list, report, k):
    report = set(report)
    answer = []
    
    # key: 신고당한 아이디, value: 신고당한횟수 
    report_dict = { i:0 for i in id_list }
    
    # key: 신고한 아이디, value: 메일발송횟수
    user_dict = { i:0 for i in id_list }
    
    # 신고당한 dict
    for i in report:
        reporting_id, reported_id = i.split()
        report_dict[reported_id] += 1
    
    # 메일발송 dict
    for i in report:
        reporting_id, reported_id = i.split()
        if report_dict[reported_id] >= k:
            user_dict[reporting_id] += 1
    
    for i in id_list:
        answer.append(user_dict[i])
        
    return answer