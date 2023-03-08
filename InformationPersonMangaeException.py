person = {}

properties = [
    ("name" , str),
    ("surname" , str),
    ("age" , int),
    ("height" , float),
    ("width" , float),
]
for prperty , p_type in properties:
    valid_value = None
    while valid_value is None:
        try:
            value = input("Please enetr your %s: " % prperty)
            valid_value = p_type(value)
        except ValueError as ve:
            print(ve)
person[property] = valid_value