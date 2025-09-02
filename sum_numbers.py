# Sum of Numbers (While Loop)
# Keep asking the user for numbers until they enter done.
# Then print the sum of all numbers entered.

ans=''
sum=0
while True:
    print('enter the number, if u are done enter done') 
    ans=input('>')
    if ans=='done':
        break
    else:
        sum=sum+int(ans)

print(f"the sum of ur numbers is {sum}")