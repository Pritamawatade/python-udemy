class Chai:
    def __init__(self, type_, strength):
        self.type_ = type_
        self.strngth = strength
        
    
# You can do it this way but this is code duplication and also break
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type_ = type_
#         self.strngth = strength
#         self.spice_level = spice_level


# Another way of doing it
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)  # calling base class constructor
        self.spice_level = spice_level
        
   
class GingerChai2(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
        
    