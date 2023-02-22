class Calculator:
    def Sum(self, a, b):
      return a + b
    def Multiply(self, a, b):
      return a * b
    def Subtraction(self, a, b):
      return a - b
    def Division(self, a, b):
      return a / b
    def Remainder(self, a, b):
      return a % b
    def Power(self, a, b):
      return a ** b
    def Quotient(self, a, b):
      return a // b
      
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
x = Calculator()
print("What do you want to perform: \n1 for Sum, \n2 for Multiplication, \n3 for Substraction, \n4 for Division, \n5 for Remainder, \n6 for Power, \n7 for Quotient?")
print()
y = int(input())
print("Your desired answer is:")
if y==1:
  print(x.Sum(a,b))
elif y==2:
  print(x.Multiply(a, b))
elif y==3:
  print(x.Subtraction(a, b))
elif y==4:
  print(x.Division(a, b))
elif y==5:
  print(x.Remainder(a, b))
elif y==6:
  print(x.Power(a, b))
elif y==7:
  print(x.Quotient(a, b))
