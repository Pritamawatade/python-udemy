class Chaicup:
    size = 1211

    def printS(self):
        return f"size = {self.size}"


cup1 = Chaicup()
print(cup1.printS())
print(Chaicup.printS(cup1))


