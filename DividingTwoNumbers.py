number1 = input("Pleasr inster first number: ")
number2 = input("Pleasr inster second number: ")


try:
    number1 = float(number1)
    number2 = float(number2)
    result = number1 / number2 
except ValueError:
    print("You must enter two numbers ")
except ZeroDivisionError:
    print("Attempt to divide by zero")

else:
    print("%.3f / %.3f = %.3f " % (number1, number2 , result))