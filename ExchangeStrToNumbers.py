
text = str(input("Please inter your string: "))

#def exchange string to numbers 
def toInteger(text):
    try:
        print("-Begin parse text:" , text)
        value = int(text)
        return value
    except ValueError as e :
        print("ValueError Message: " , str(e))
        print("type(e): ", type(e))
        return 0
    finally:
        print("-End parse text: " , text)


value = toInteger(text)
print("value: " , value)

