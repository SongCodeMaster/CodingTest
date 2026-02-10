def solution(bandage, health, attacks):
    t = bandage[0] # 시전 시간
    x = bandage[1] # 초당 회복량
    y = bandage[2] # 추가 회복량
    
    my_health = health 
    last_attack_time = 0 
    
    for i in attacks:
        attack_time = i[0]
        damage = i[1]
        
        # 1. 공격 받기 전까지의 시간(초) 구하기
        gap_time = attack_time - last_attack_time - 1 
        
        # 2. 회복량 계산 (기본 회복 + 추가 회복)
        # 몫(//)을 구해서 추가 회복 횟수를 곱해줍니다.
        bonus_recovery = (gap_time // t) * y
        total_heal = (gap_time * x) + bonus_recovery
        
        # 3. 체력 회복 적용
        my_health += total_heal
        
        # 4. 최대 체력 초과 방지 (if문 대신 min을 쓰면 깔끔합니다)
        if my_health > health:
            my_health = health
            
        # 5. 공격 받음 (continue 없이 무조건 맞아야 함)
        my_health -= damage
        
        # 6. 사망 여부 확인
        if my_health <= 0:
            return -1
        
        # 7. 마지막 공격 시간 갱신
        last_attack_time = attack_time
        
    return my_health