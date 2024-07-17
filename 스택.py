import sys

num = int(sys.stdin.readline())
stack=[]
for i in range (num):
  comment=sys.stdin.readline().split()
  if comment[0]=='push':
    stack.append(comment[1])
  if comment[0]=='pop':
    if(len(stack)==0):
      print('-1')
    else:
      print(stack.pop())
  if comment[0]=='size':
    print(len(stack))
  if comment[0]=='empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  if comment[0]=='top':
    if len(stack)==0:
      print(-1)
    else: print(stack[-1])