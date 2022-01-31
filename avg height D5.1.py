# average Height
height = input("Enter the height followed by space \n").split()
for i in range (0, len(height)):
    height[i] = int(height[i])
avg = round((sum(height))/len(height))

print(avg)