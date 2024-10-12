# Basic
for int in range(151):
    print(int)

# Multiples of Five
for int in range(1001):
    if (int%5 ==0):
        print(int)

# Counting, the Dojo Way
for int in range(1,101):
    if (int%10 ==0):
        print("Coding Dojo")
    elif(int%5 ==0):
        print("Coding")

# Whoa. That Sucker's Huge
sum = 0
for int in range(500001):
    if (int%2!=0):
        sum += int
print(sum)

# Countdown by Fours
for int in range(2018, 0, -4):
    print(int)

# Flexible Counter
low_num = 2
high_num = 90
mult = 3
for int in range(low_num, high_num+1):
    if (int%mult ==0):
        print(int)