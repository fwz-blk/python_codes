# Print all the numbers from 1 to 100 that are divisible by both 3 and 5.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(f'{i}')