import sys

n=int(sys.stdin.readline())
equation=sys.stdin.readline()
number=dict()
stack=[]
for i in range(n):
  number[chr(65+i)]= float(input())
for j in range(len(equation)-1):
  if equation[j]=="*" :
    second, first=stack.pop(), stack.pop()
    stack.append(first*second)
  elif equation[j]=="/" :
    second, first=stack.pop(), stack.pop()
    stack.append(first/second)
  elif equation[j]=="+" :
    second, first=stack.pop(), stack.pop()
    stack.append(first+second)
  elif equation[j]=="-" :
    second, first=stack.pop(), stack.pop()
    stack.append(first-second)
  else:
    stack.append(number[equation[j]])
print("%.2f"%stack.pop())
#print(round(stack.pop(),2))