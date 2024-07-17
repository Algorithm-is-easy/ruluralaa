n = int(input())
li=list(map(int, input().split()))

psum=[0]*(n+1)
answer=[0]*(n+1)
for i in range(1, n+1):
  psum[i]=li[i-1]*(i)
  answer[i]=psum[i]-psum[i-1]
for i in range(1, n+1):
  print(answer[i], end=" ")