import sys

n = int(sys.stdin.readline())
stack=[]
pop=[]
count =1
isNo= False

for _ in range(n):
  num= int(sys.stdin.readline())
  while(count<=num):
    stack.append(count)
    pop.append('+')
    count=count+1
    
  if stack[-1]==num:
    pop.append('-')
    stack.pop()
  else:
    isNo= True
    break
  
if isNo==True:
  print('NO')
else:
  for i in pop:
    print(i)