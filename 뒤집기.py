s=input()
#문자열에서 연속된 1의 덩이리 개수 구하기
#문제열에서 연속된 0의 덩어리 개수 구하기
#위에서 구한 개수 중 더 작은 개수 출력
cntZero=0
cntOne=0
for i in range(len(s)):
  if i==len(s)-1:
    if s[i]=="1":
        cntOne=cntOne+1
    if s[i]=="0":
        cntZero=cntZero+1
  else:
    if s[i]!=s[i+1]:
      if s[i]=="1":
          cntOne=cntOne+1
      if s[i]=="0":
          cntZero=cntZero+1
if cntZero >= cntOne:
  print(cntOne)
else:
  print(cntZero)
