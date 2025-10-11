def floatValidate(input):
    try:
     return float(input)
    except ValueError:
         return False

def intValidate(input):
    try:
     return int(input)
    except ValueError:
         return False


def strValidate(input):
    try:
     return str(input)
    except ValueError:
         return False
 