'''Write a class “Calculator” capable of finding square,
 cube and square root of a number'''

class Calculator:
   

    def calculate(self, number):
        print(f"Square of {number}: {number**2}")
        print(f"Cube of {number}: {number**3}")
        print(f"Square-root of {number}: {number**0.5}")

number = int(input("enter a number: "))
result = Calculator()
result.calculate(number)