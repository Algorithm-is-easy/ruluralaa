def solution(array, commands):
    answer = []
    for i in commands:
        start=i[0]-1
        end=i[1]
        order=i[2]-1
        slicing=array[start:end]
        slicing.sort()
        answer.append(slicing[order])
    
    return answer
  
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
answer=solution(array, commands)
print(answer)