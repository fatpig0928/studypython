'''策略模式'''

class Credit():
    def __init__(self):
        pass

    def chargebacks(self, price):
        print('花费了', price, '人民币')

#抽象基类   
class Pos():
    def __init__(self):
        pass

    def paybycard(self,price,credit):
        credit.chargebacks(price)   

#第一个具体策略
class CnyPos(Pos):
    
    def paybycard(self,price,credit):
        credit.chargebacks(price)  

#第二个具体策略
class UsdPos(Pos):

    def paybycard(self,price,credit):
        price = price * 7
        credit.chargebacks(price)  

#第三个具体策略
class JpyPos(Pos):

    def paybycard(self,price,credit):
        price = price * 1/100 * (1 + 15/1000) * 7
        credit.chargebacks(price)  

#第四个具体策略
class EURPos(Pos):

    def paybycard(self,price,credit):
        price = price * 1.2 * (1 + 15/1000) *7
        credit.chargebacks(price)  
     
class Store():
    def __init__(self,pos):
        self.pos = pos

    def pay(self, price, credit):
        self.pos.paybycard(price,credit)

if __name__ == '__main__':
    credit = Credit()

    cnypos = CnyPos()
    usdpos = UsdPos()
    jpypos = JpyPos()
    eurpos = EURPos()

    zara = Store(cnypos)
    hm = Store(usdpos)
    hstyle = Store(jpypos)
    haha = Store(eurpos)

    zara.pay(500, credit)
    hm.pay(500, credit)
    hstyle.pay(500, credit)
    haha.pay(500, credit)



    


