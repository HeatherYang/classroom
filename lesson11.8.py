#coding:utf-8
class Medal(object):
    def __init__(self,country,num1,num2,num3):
        self.area = country
        self.gold = num1
        self.silver = num2
        self.copper = num3

    def get_place(self,placing):
        if placing==1:
            self.gold+=1
        elif placing==2:
            self.silver+=1
        else:
            self.copper+=1

    @property
    def count(self):
        return self.gold+self.silver+self.copper

    def __str__(self):
        return '%s 金牌：%d，银牌：%d，铜牌：%d，总计：%d' % (
            self.area,self.gold, self.silver, self.copper,self.count
        )


China=Medal('中国',26,17,26)
UK=Medal('英国',27,23,16)
US=Medal('美国',45,37,38)
US.get_place(1)
China.get_place(2)
UK.get_place(3)
print China
print UK
print US
ranking=[China,UK,US]
GOLD=sorted(ranking,key=lambda x:x.gold,reverse=True)
SUM=sorted(ranking,key=lambda  x:x.count,reverse=True)
print '按金牌排序'
for g in GOLD:
    print g
print '按总数排序'
for s in SUM:
    print s










