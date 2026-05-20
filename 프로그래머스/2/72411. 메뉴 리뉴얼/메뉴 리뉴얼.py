# order에서 course수만큼 조합을 뽑는다.
# 코스 조합에서 가장 많이 주문된 메뉴 찾아서 2명 이상이면 정답 배열에 추가
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for courses in course: # 코스조합
        courses_dict = defaultdict(int)
        for order in orders: # 코스배열에서
            sort_order = sorted(order)
            for combi_order in combinations(sort_order, courses): # 조합튜플생성
                courses_dict[''.join(combi_order)] += 1
            
        
        # 코스중에 가장 많은 조합 찾기
        if courses_dict:
            max_count = max(courses_dict.values())
        
            if max_count >= 2:
                for menu, count in courses_dict.items():
                    if count == max_count:
                        answer.append(menu)
            
    
    return sorted(answer)