
order_amount = int(input("please enter order amount:"))

delevery_fee = 0 if order_amount > 300 else 30
# what the above code will do is if the order_amount is greater than 300 it will store 0  in delevery_fee and 30 if not. this is how ternary operator looks in python

print(f"delevery_fee = {delevery_fee}")
# the value of delevery_fee will depend on the ternary condition

