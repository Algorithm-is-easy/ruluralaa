#입력
n=int(input())
li=list(map(int, input().split()))

#내림차순 정렬
li.sort(reverse=True)
count=[0]*n

for i in range(n):
    count[i]=li[i]+i+1
count.sort(reverse=True)
solution=count[0]
print(solution+1) # 시작일이 1일이므로 1추가