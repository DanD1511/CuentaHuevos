class Operations:
    def __init__(self, count=0):
        self.count = count

    def add(self, amount):
        self.count += amount

    def subtract(self, amount):
        self.count -= amount

    def multiply(self, amount):
        self.count *= amount

    def divide(self, amount):
        if amount != 0:
            self.count /= amount
        else:
            raise ValueError("Cannot divide by zero")

    def get_count(self):
        return self.count
