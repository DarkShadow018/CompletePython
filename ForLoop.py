number1 = int(input("Enter the starting range : "))
number2 = int(input("Enter the last number of the range : "))

for number1 in range(number2):
    print(number1 + 1)

number4 = int(input("Enter the starting range : "))
number3 = int(input("Enter the ending of the range : "))

for number4 in range(number3):
    print((number4 + 1) * "* ")
    number3 += 1

#number5 = int(input("Enter the starting range : "))
#number6 = int(input("Enter the ending of the range : "))

#for number5 in range(number6):
#    print(number5 * "* ")
#    number5 -= 1