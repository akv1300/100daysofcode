# Password generator project
P_letters = int(input("How many letters do you want?"))
P_symbols = int(input("How many symbols do you want?"))
P_numbers = int(input("How many numbers do you want?"))

list1 = []
letters = ["a", "c", "D", "A","F"]
symbols = ["!", "@","#", "$", "%"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
import random
for i in range( 0 ,P_letters):
    list1.append(random.choice(letters))
for i in range( 0 ,P_symbols):
    list1.append(random.choice(symbols))
for i in range( 0 ,P_numbers):
    list1.append(random.choice(numbers))
passw = []
for i in range (0,len(list1)):
    key = random.choice(list1)
    passw.append(str(key))
    list1.remove(key)
print("".join(passw))