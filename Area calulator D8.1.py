import math
height = int(input("Enter height \n"))
width = int(input("Enter width \n"))
cover = 5
def no_of_can (height, width, cover):
    print(math.ceil((height * width)/cover))
no_of_can(height, width, cover)
