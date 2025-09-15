class BaseChai:
    def __init__(self, type_) -> None:
        self.type_ = type_

    def prepare(self):
        return f"prepare {self.type_} chai...."

class MasalaChai(BaseChai):
    def add_spices(self):
        print("add spices")

class Chai_shop:
    chai_cls = BaseChai # this is composition, you are inherinting all the values of base chai

    def __init__(self) -> None:
        self.chai = self.chai_cls("regular")

    def serve(self):
        print(f"serving {self.chai.type_}")
        self.chai.prepare()
    
class FancyChaiShop(Chai_shop):
    chai_cls = MasalaChai
    

shop = Chai_shop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()