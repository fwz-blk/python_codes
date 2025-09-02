# 2. Multiplication Table (For Loop)
# Ask the user for a number n. Print the multiplication table of n up to 10.
print('enter the number to print the table of')
num=int(input("->"))

for i in range(1,11):
    ans=i*num
    print(f"{i} x {num} = {ans}")