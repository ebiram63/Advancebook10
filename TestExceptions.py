import random


class Error(Exception):
    """ Base class for other exceptions """
    pass

#Define class for NegativeValueError
class NegativeValueError(Error):
    """Raised when the input is negative"""
    pass

#define class for ValueTooSmallError
class ValueTooSmallError(Error):
    """Raised when the input is too small"""
    pass

#define class for ValueTooLargeError
class ValueTooLargeError(Error):
    """Raised when the input is too large"""
    pass

number = 20
#number = random(1,999)
while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegativeValueError
        elif num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        break 
    except NegativeValueError:
        print("This is Negative Value, try again")
        print("")
    except ValueTooSmallError:
        print("This Value is Too Small, try again")
        print("")
    except ValueTooLargeError:
        print("This Value is Too Large, try again")
        print("")
print("Correct Value Entered")

