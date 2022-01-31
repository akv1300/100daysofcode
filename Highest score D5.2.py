# Highest Score
score = input("Enter score followed by space \n").split()
for i in range (0, len(score)):
    score[i] = int(score[i])
highest_score = 0
for i in score:
    if i>highest_score:
        highest_score = i
    else:
        continue
print(highest_score) 