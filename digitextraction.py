x=int(input("enter the number:"))
y=x

while x>0:
    d=x%10
    x=x//10
    print(f"the digit is {d}")