
def solution(s):
    num_dict = {"one" : 1,"two":2 ,"three":3,"four":4 , "five":5, "six": 6, "seven":7,"eight" :8, "nine":9, "zero":0}
    for i in num_dict.keys() :
        if i in s :
            s=s.replace(i,str(num_dict[i]))
            
    return int(s)

  
solution("one4seveneight")

# https://monicareport.tistory.com/654
# https://blog.naver.com/dororong0222/223049746239