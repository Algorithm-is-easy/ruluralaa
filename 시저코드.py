def solution(s, n):
    num=0
    sentense=[]
    answer=''
    for x in s:
        if(65<=ord(x)<=90):
            num=ord(x)+n
            if(num>90):
                num=num-26
            sentense.append(chr(num))
        if(97<=ord(x)<=122):
            num=ord(x)+n
            if(num>122):
                num=num-26
            sentense.append(chr(num))
        if(x==" "):           
            sentense.append(x)                            
    for y in sentense:
        answer += y
    return answer

solution("z",1)