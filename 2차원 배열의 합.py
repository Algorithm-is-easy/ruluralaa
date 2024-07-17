n, m=map(int,input().split())
li=[[0 for j in range(m)]for i in range(n)]
psum=[[0 for j in range(m+1)]for i in range(n+1)]
for i in range(n):
  li[i]=list(map(int, input().split()))
for i in range(1,n+1):
  for j in range(1, m+1):
    if i!=1 and j==1:
      psum[i][j]=psum[i-1][m]+li[i-1][j-1]
    else:
      psum[i][j]=psum[i][j-1]+li[i-1][j-1]
k=int(input())
answer=[0]*k
for l in range(k):
  i,j,x,y=map(int,input().split())
  if i!=1 and j==1:
    answer[l]=psum[x][y]-psum[i-1][m]
  else:
    answer[l]=psum[x][y]-psum[i][j-1]
for ans in answer:
  print(ans)
