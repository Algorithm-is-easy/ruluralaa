import sys

left=list(sys.stdin.readline().rstrip())
right=[]
n=int(sys.stdin.readline())
for i in range(n):
   command=list(sys.stdin.readline().split())
   if command[0]=="L":
     if left:
      right.append(left.pop())
   elif command[0]=="D":
     if right:
       left.append(right.pop())
   elif command[0]=="B":
     if left:
       left.pop()
   else:
     left.append(command[1])
left.extend(reversed(right))
print(''.join(left))