class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        return self.num1 / self.num2
try:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    calc = Calculator(a, b)
    
    
    if op == '+':
        print("Sum:", calc.add())
    elif op == '-':
        print("Difference:", calc.subtract())
    elif op == '*':
        print("Multiplication:", calc.multiply())
    elif op == '/':
        print("Answer:", calc.divide())
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input.")


