import sys

n=int(sys.stdin.readline())
li=[]
for i in range(n):
  li.append(int(sys.stdin.readline()))
  
li.sort()
complain=0
for i in range(n):
  if li[i]!=i+1:
    complain+=abs((i+1)-li[i])
print(complain)