num=int(input("enter the 3 digit number:"))

copy=num

d1=num%10

num=num//10

d2=num%10

num=num//10

d3=num%10

cube=(d1)**3+(d2)**3+(d2)**3

if num==cube:
    print('the number is armstrong')
else:
    print('the number aint armstrong')

