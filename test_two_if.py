from numpy import *
start = 100
probability_win = 60
kelly = (probability_win*1/100-(100-probability_win)*1/100)/(1*1)
cang_wei = kelly



def get_final(cang_wei,probability_win):
    random.seed()
    global start
    for i in range(1000):
        rand = random.randint(0, 100)
        if rand < (100-probability_win):
            start = start * (1 - cang_wei)
        else:
            start = start * (1 + cang_wei)
    return start



final_start1 = get_final(cang_wei= kelly,probability_win=60)
print(final_start1)

final_start2 = get_final(cang_wei= 0.1, probability_win=60)
print(final_start2)

final_start3 = get_final(cang_wei= 0.3, probability_win=60)
print(final_start3)




