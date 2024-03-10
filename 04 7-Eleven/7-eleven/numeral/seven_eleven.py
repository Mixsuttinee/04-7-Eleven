# seven_eleven.py

def to_seven_eleven(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num % 7 == 0 and num % 11 == 0:
        return "7-Eleven"
    elif num % 7 == 0:
        return "seven"
    elif num % 11 == 0:
        return "eleven"
    else:
        return str(num)
