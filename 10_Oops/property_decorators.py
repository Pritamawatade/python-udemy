class Tealead:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if age < 18:
            print("You are not eligible")   
        else:
            self._age = age

        
        
t = Tealead(3)


print(t.age)

t.age = 12
print(t.age)