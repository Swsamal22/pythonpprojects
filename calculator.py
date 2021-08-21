class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def Sum(self):
        return self.a+self.b
    
    def Sub(self):
        return self.a-self.b

    def Mul(self):
        return self.a*self.b
    
    def Div(self):
        return self.a/self.b

    def Power(self):
        return self.a**self.b

print()
print("Welcome to the Calculator !")
print()
#highlighting the format for operation as for substraction and division the first number neeeds to be greater than the second number
print("Enter the number where A is greater than B")
print()
print("Enter the first number: ")
num1 = float(input())
print("Enter the operator: 1) '+' 2) '-' 3) '*' 4) '/' 5) '^' ")
op = input()
print("Enter the second number: ")
num2 = float(input())

c=calculator(num1,num2)

#choosing the operation
if op == "+":
    print("The result is: {0:.4f}".format(c.Sum()))
elif op == "-":
    print("The result is: {0:.4f}".format(c.Sub()))
elif op == "*":
    print("The result is: {0:.4f}".format(c.Mul()))
elif op == "/":
    print("The result is: {0:.4f}".format(c.Div()))
elif op == "^":
    print("The result is: {0:.4f}".format(c.Power()))
else:
    print("Invalid operator")

