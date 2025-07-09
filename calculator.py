class Calculator:
    def __init__(self, num1, num2=None):
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
    
    def square(self):
        return self.num1 ** 2
    
    def square_root(self):
        if self.num1 < 0:
            return "Cannot calculate square root of negative number"
        return self.num1 ** 0.5
try:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /, square, sqrt): ")
    
    if op in ['+','-', '*', '/']:
        b = float(input("Enter second number: "))
        calc = Calculator(a, b)
    else:
        calc = Calculator(a)
    
    if op == '+':
        print("Sum:", calc.add())
    elif op == '-':
        print("Difference:", calc.subtract())
    elif op == '*':
        print("Multiplication:", calc.multiply())
    elif op == '/':
        print("Answer:", calc.divide())
    elif op == 'square':
        print("Square of first number:", calc.square())
    elif op == 'sqrt':
        print("Square root of first number:", calc.square_root())
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input.")


