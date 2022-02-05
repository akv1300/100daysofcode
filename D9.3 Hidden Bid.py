
cont = True
dic = {}
while cont:
   # print("\033[H\033[J") 
    name = input("What is your name? \n")
    bid = int(input("What's your bid \n"))
    dic[bid] = name
    Next = input("Is there anyone left. Yes or No")
    if Next == "No":
        cont = False
    else:
        print("\033[H\033[J") 
bids = max(list(dic.keys()))
print(" The bid goes to", dic[bids])