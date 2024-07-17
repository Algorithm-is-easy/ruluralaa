

def two(num,n):
  answer=[]
  while True:
    answer.append(num%2)
    num=num//2
    if num==0:
      break

  addzero=n-len(answer)
  if addzero>0:
    for i in range(addzero):
      answer.append(0)
  answer.reverse()
  return answer

def solution(n, arr1, arr2):
  two_arr1=[]
  two_arr2=[]
  for x in arr1:
    two_arr1.append(two(x,n))
  for y in arr2:
    two_arr2.append(two(y,n))
  two_arr=two_arr1
  for i in range(n):
    for j in range(n): 
      if two_arr1[i][j]==0 and two_arr2[i][j]==0:
        two_arr[i][j]=" "
      else:
          two_arr[i][j]="#"
  #리스트 문자열로 변환
  result = ""
  answer=[]
  for i in range(0,n):
    for j in range(0,n):
      for s in two_arr[i][j]:
        result += s
    answer.append(result)
    result = ""
  return answer
# https://minnit-develop.tistory.com/17
# https://codetorial.net/tips_and_examples/reverse_python_list_or_numpy_array.html
# https://blockdmask.tistory.com/573

n=5
arr1	=[9, 20, 28, 18, 11]
arr2	=[30, 1, 21, 17, 28]
solution(n, arr1, arr2)