total = 0

num1 = int(input('choose your first number:'))
num2 = int(input('choose your second number:'))


if num1 < num2:
    for num in range(num1,(num2+1)):
        ten = num * 10
        total += ten
        print(f'{num}\t{ten}')


else:
    for num in range(num2,(num1+1)):
        ten = num * 10
        total += ten
        print(f'{num}\t{ten}')
print(f'The total is {total}.')