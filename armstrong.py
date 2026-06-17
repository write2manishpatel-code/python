number = int(input("enter a number"))
sum = 0

temp = number

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10


if number == sum:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")
