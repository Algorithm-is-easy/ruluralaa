t=["0"]*1000001
t[1]="1"
t.append([])
t[2].append("11")
t[2].append("00")
def tile(num):
  if num==1: return t[1]
  if num==2: return t[2]
  if t[num-1] == 0: return tile(num-1)
  if t[num-2] ==0: return tile(num-2)
  for i in t[num-1]:
    n=[]
    n.append("1"+t[num-1][i])
  for j in t[num-2]:
    m=[]
    m.append("00"+t[num-2][j])
  n.extend(m)
  t[num]=n  
  return t[num]

num=input()
tile(3)
# result=len(tile(num))
# print(result%15746)