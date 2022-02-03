# ceaser cypher
import string
conti = True
while conti:
    alpha = list((string.ascii_letters).lower())
    word = input("Feed data \n")
    word = word.lower()
    key = int(input("Enter the number of shift you want \n"))
    direction = input("Do you want to encrpyt or decrypt")
    if key > 26:
        key = key%26
    def ceaser (word, key, direction):
        new_word = ""
        if direction == "encrypt":
            for i in word:
                if i.islower():
                    position = alpha.index(i)
                    position = position + key
                    new_word += alpha[position]
                else:
                    new_word+=i
            print(new_word)
        elif direction == "decrypt":
            alpha.reverse()
            for i in word:
                if i.islower():
                    position = alpha.index(i)
                    position = position + key
                    new_word += alpha[position]
                else:
                    new_word+=i
            print(new_word)
    ceaser (word, key, direction)
    cont = input("Do you want to restart. True or False")  
    if cont == "False":
        conti = False
    