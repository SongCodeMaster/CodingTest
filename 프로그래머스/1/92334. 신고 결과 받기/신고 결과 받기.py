def solution(id_list, report, k):
    answer = []
    report = set(report)
    reporting_user = { i:0 for i in id_list }
    reported_user = { j:0 for j in id_list }
    
    # reported
    for user in report:
        my_user = user.split(' ')
        reporting = my_user[0]
        reported = my_user[1]
        
        reported_user[reported] += 1
        
    # reporting
    for user in report:
        my_user = user.split(' ')
        reporting = my_user[0]
        reported = my_user[1]
        
        if reported_user[reported] >= k:
            reporting_user[reporting] += 1
    
    for key, value in reporting_user.items():
        answer.append(value)
    return answer