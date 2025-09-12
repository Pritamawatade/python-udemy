def chai_order():
    print("What chai do you want : ")
    order = yield

    while(True):
        print(f"Your order = {order}")
        order = yield

chai = chai_order()
next(chai) # start the generator    

chai.send("masala")
chai.send("cardimom")
chai.send("ginger")