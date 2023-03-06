print("Three")
value = 10 / 2
print("Two")
value = 10 / 1
print("One")
d = 0
try:
    #this dicision has problem, divided by 0
    # An error has occured here (ZeroDivisionError).
    value = 10 / d
    print("value = ", value)

except ZeroDivisionError as e:
    print("Error: ", str(e))
    print("Ignore to continue ...")
print("Let's go!")

