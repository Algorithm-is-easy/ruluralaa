N, M=map(int, input().split())
Nli=list(map(int,input().split()))
psum=[0]*(N+1) #0~N
for i in range(1, N+1): #1~N
  psum[i]=psum[i-1]+Nli[i-1]
answer=[0]*M
for k in range(M):
  i, j = map(int,input().split())
  answer[k]=psum[j]-psum[i-1]
for i in range(M):
  print(answer[i])