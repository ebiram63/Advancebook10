Num_list = []

for i in range(1,6):
    try:
        Num_list.append(int(input("Please enter your numbers: ")))
        i += 1
    except TypeError:
        print("The number is not able to be empty") 
#print(Num_list)

num = int(input("Please enter your number: "))

for b in Num_list:
    try:
        c = num / b
        print(c)
    except ZeroDivisionError:
        print("An elemnt with 0 value")
    except TypeError:
        print("Only numbers can be used")