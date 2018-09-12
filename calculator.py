class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x/y

calculator = Calculator()
print("1 + 2 = ....")
print(calculator.add(1,2))
print("1 - 2 = ....")
print(calculator.subtract(1,2))
