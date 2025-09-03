# Write a program to reverse a number (e.g., 123 → 321).
print('enter the number u want to reverse')
x=int(input('->'))
rev=0
while x>0 :
    digit=x%10
    x=x//10
    rev=rev*10+digit

print(f"ur reversed number is {rev}")