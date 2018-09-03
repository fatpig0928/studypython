'''策略模式'''

#抽象基类   
class Pos():
    def __init__(self):
        pass

    def paybycard(self,price,credit):
        credit.chargebacks(price)   

#第一个具体策略
class CnyPos(Pos):
    
    def paybycard(self,price):
        return  

#第二个具体策略
class UsdPos(Pos):

    def paybycard(self,price):
        return price * 7

#第三个具体策略
class JpyPos(Pos):

    def paybycard(self,price):
        return price * 1/100 * (1 + 15/1000) * 7 

#第四个具体策略
class EURPos(Pos):

    def paybycard(self,price):
        return price * 1.2 * (1 + 15/1000) *7 
     
class Store():
    def __init__(self,pos):
        self.pos = pos

    def pay(self, price):
        return self.pos.paybycard(price)

if __name__ == '__main__':

    zara = Store(CnyPos())
    hm = Store(UsdPos())
    hstyle = Store(JpyPos())
    haha = Store(EURPos())

    print(zara.pay(500))
    print(hm.pay(500))
    print(hstyle.pay(500))
    print(haha.pay(500))



    


