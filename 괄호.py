import sys

n=int(sys.stdin.readline())
for i in range(n):
  left=0
  right=0
  command=sys.stdin.readline()
  
  for j in range(len(command)):
    if command[j]=='(':
      left=left+1
    else :
      right=right+1
    
    if left<right:
      print("NO")
      break
      
  if left==right:
    # if left==0 and right==0:
    #   print('NO')
    # else: 
    print('YES')
  elif left>right:
    print('NO')
    
  