class Stall:
    def __init__(self, type_, chai_size):
        self.chai_type = type_,
        self.chai_size = chai_size

    def show(self):
        return f"chai type = {self.chai_type}\n chai size = {self.chai_size}"


order = Stall("masala", "200ml")

print(order.show())