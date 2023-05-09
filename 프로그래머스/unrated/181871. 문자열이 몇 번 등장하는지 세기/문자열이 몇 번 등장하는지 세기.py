def solution(myString, pat):
    count = 0 
    start = 0
    
    while True:
        start = myString.find(pat,start)+1
        if start>0:
            count+=1
        else:
            return count