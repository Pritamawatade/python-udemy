class Exc:
    
    def test(self, age):
        try:
            if age < 18:
                raise ValueError("Age is not valid")
            print("Welcome to vote")
        except ValueError as e:
            print(e)
            print("You are not allowed to vote")
        else:
            print("No exception")
        finally:            
            print("Execution completed")
            print("Thank you")
            
            
e = Exc()
e.test(1)