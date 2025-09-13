class Chai:
    origin = "india"

print(Chai.origin)
print(type(Chai))

Chai.milk = False;

print(Chai.milk)

# creating object

chai = Chai()
print("origin fomr obj",chai.origin)
chai.milk = True;
print("milk fomr class", Chai.milk)