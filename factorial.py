# Write a program to calculate the factorial of a number using a loop.
print("enter the number u want factorial of")
x=int(input('->')) 
fact=1;
for  i in range(1,x+1):
    fact=fact*i

print(f"ur factorial is {fact}")
