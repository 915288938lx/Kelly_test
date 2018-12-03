import numpy as np
from matplotlib import pyplot as plt
def get_specific_out(): #按照给定频率序列【0.6,0.4】， 生成随机序列【-1,1】

    p = np.array([0.6,0.4])
    index = np.random.choice([1,-1], p=p.ravel())
    return index

def get_final(cangwei): #计算在某一仓位下， 以频率序列【0.6,0.4】，生成1000个随机序列【-1,1】， 得到的最终资产
    money = 100

    for i in range(1000):
        rand = get_specific_out()
        if rand == 1:
            money = money * (1 + cangwei)
        else:
            money = money * (1 - cangwei)
    return money




def get_max_money(): # 获取[0,0.01,0.02,..0.99]100个仓位中， 出现最大最终资产的仓位值以及资产值
    np.random.seed()
    maxmoney = 0
    cangwei = 0
    for i in [x / 100 for x in range(1, 100)]: #生成[0,0.01,0.02,..0.99] 100个仓位数字
        money = get_final(i) # 返回在100个不同仓位下的最终资产
        print('仓位为%s，最终资产为：%s'%(i,money))
        if money >= maxmoney:
            maxmoney = money # 得到最大最终资产
            cangwei = i # 得到最大最终资产所用的仓位


    return maxmoney,cangwei




def get_multi_run(): #重复此过程100次，统计每次最大最终资产的仓位值
    for i in range(200):
        print('第%s次运行过程\n'%i)
        maxmoney, cangwei  =  get_max_money()
        yield cangwei

def count_each_max_cangwei():
    multi_run = get_multi_run()
    multi_run_maxs_array = np.array(list(multi_run))
    times_ = []
    for cw in [x / 100 for x in range(1, 100)]:
        times =np.sum(multi_run_maxs_array == cw)
        print('仓位为%s的个数为：%s'%(cw,times))
        times_.append(times)
    x_pos = [x / 100 for x in range(1, 100)]
    plt.bar(x_pos, times_, align='center', alpha=1)
    plt.title('频率分布')
    plt.xlabel('仓位')
    plt.ylabel('出现最大值的次数')
    plt.show()
if __name__ == '__main__':
    count_each_max_cangwei()








