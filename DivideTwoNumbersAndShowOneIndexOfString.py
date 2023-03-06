num1 = int(input("Insert your first number: "))
num2 = int(input("Insert your second number: "))
character = input("Enter your character: ")

try:
    value = num1 / num2
    print(character[int(value)])
except(IndexError, ValueError) as e:
    print("An error occurred: " , e)



