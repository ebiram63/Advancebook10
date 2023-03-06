Entr1 = str(input("First Enterence: "))
Entr2 = str(input("Second Enterence: "))
Entr3 = str(input("Third Enterence: "))
Entr4 = str(input("Fourth Enterence: "))

variable = [Entr1, Entr2, Entr3, Entr4]

for i in variable:
    print("===============")
    try:
        if float(i):
            print("Attempting to convert" , i , "-->",) 
            print(float(i))  
        else:
            print("Error: ", i )  

    except (TypeError):
        print("I can only convert a string or a number!")
        continue
    except (ValueError):
        print("I can only convert a string of digitd! ")
        continue

    