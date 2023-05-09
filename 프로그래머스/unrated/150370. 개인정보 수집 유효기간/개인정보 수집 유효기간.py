from datetime import datetime,timedelta

def solution(today, terms, privacies):
    answer = []
    dic = {}
    year,month,day = today.split('.')
    today = datetime(int(year),int(month),int(day))
    for term in terms:
        t,month = term.split()
        dic[t] = int(month)
    for i in range(len(privacies)):
        date,t = privacies[i].split()
        year,month,day = date.split('.')
        
        if (int(month)+dic[t])>12:
            year = int(year)+(int(month)+dic[t])//12
            month = (int(month)+dic[t])%12
            if month == 0:
                year -= 1
                month = 12
            day = int(day)
        else:
            year = int(year)
            month = (int(month)+dic[t])
            day = int(day)
        
        date = datetime(year,month,day)
        
        if today >= date:
            answer.append(i+1)
        
    return answer