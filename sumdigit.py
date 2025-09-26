x=int(input("enter the number:"))
y=x
osum=esum=0
while x>0:
    d=x%10
    x=x//10
    if d % 2 == 0:
        esum=esum+d
    elif d % 2 != 0:
        osum=osum+d
        


print(f"the sum of the even digits of the number {y} is {esum}")
print(f"the sum of the odd digits of the number {y} is {osum}")