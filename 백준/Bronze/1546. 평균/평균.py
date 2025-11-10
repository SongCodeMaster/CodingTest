n = int(input())
mylist = list(map(int, input().split())) # 점수 리스트로 받기
mymax = max(mylist) # 최댓값 뽑기
sum = sum(mylist)

print(sum*100/n/mymax)