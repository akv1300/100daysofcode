#prime number checker
import math
def prime_number_check(number):
    sqr_num = int(math.sqrt(number))
    count = 0
    for i in range (2,sqr_num+1):
        if number%i == 0:
            count+=1
    if count == 0:
        print(number, "is prime")
    else:
        print(number, "is not prime")
number = int(input("Enter your number \n"))
prime_number_check(number)