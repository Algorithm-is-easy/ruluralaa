import sys

n=int(sys.stdin.readline())
stack=[]
sum=0
for i in range(n):
  number=int(sys.stdin.readline())
  if number==0:
    stack.pop()
  else:
    stack.append(number)
for i in stack:
  sum=sum+i
print(sum)