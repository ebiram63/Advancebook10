Entr1 = input("First Enterence: ")
Entr2 = input("Second Enterence: ")
Entr3 = input("Third Enterence: ")
Entr4 = input("Fourth Enterence: ")

variable = [Entr1, Entr2, Entr3, Entr4]

for i in variable:
    print("===============")
    try:
        if type(i) != float:
            print("Error: ", i )
        print("Attempting to convert" , i , "-->",) 
        print(float(i))    

    except TypeError as e:
        print("I can only convert a string or a number!")
        continue
    except ValueError as e:
        print("I can only convert a string of digitd! ")
        continue

    