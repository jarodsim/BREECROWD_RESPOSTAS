# -*- coding: utf-8 -*-

#Execução: python3 script.py < input.txt

def check_penaltis(time1_1,time1_2,time2_1,time2_2):
    # 1 - saldo total de gols
    saldo_1 = (time1_1+time1_2) - (time2_1+time2_2)
    saldo_2 = (time2_1+time2_2) - (time1_1+time1_2)
    if not saldo_1==saldo_2:
        return 'Time 1' if (saldo_1>saldo_2) else 'Time 2'
        
    # 2 - saldo gols no adversário
    if not time2_1==time1_2:
        return 'Time 1' if (time1_2>time2_1) else 'Time 2'
        
    
    return 'Penaltis'

def return_pontuation(a,b):
    if a==b:
        return 1
    else:
        return 3 if a>b else 0
    
def find_winner():
    #time1_1 time 1 jogou em casa, time2_1 time 2 jogou na casa do time 1
    time1_1, time2_1 = list(map(int,input().split("x")))

    point1, point2 = return_pontuation(time1_1, time2_1), return_pontuation(time2_1, time1_1)
    
    time2_2, time1_2 = list(map(int,input().split("x")))
    point1 += return_pontuation(time1_2, time2_2)
    point2 += return_pontuation(time2_2, time1_2)
        
    if point1 > point2:
        return 'Time 1'
    elif point2 > point1:
        return 'Time 2'
    else:
        return check_penaltis(time1_1,time1_2,time2_1,time2_2)
    

for i in range(int(input())):
   print(find_winner())