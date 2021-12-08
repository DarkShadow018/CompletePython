first = float(input("Enter first number : "))
operator = (input("Enter a valid operator : "))
second = float(input("Enter second number : "))

if operator == '+' or operator == 'Addition' or operator == 'addition' or operator == 'Add' or operator == 'add':
    print(first + second)
if operator == '-' or operator == 'Subtract' or operator == 'subtract' or operator == 'Sub' or operator == 'sub':
    print(first - second)
if operator == '*' or operator == 'Multiply' or operator == 'multiply' or operator == 'Mul' or operator == 'mul':
    print(first * second)
if operator == '/' or operator == 'Divide' or operator == 'divide' or operator == 'Div' or operator == 'div':
    print(first / second)
if operator == '%' or operator == 'Mod' or operator == 'mod' :
    print(first % second)
if operator == '**' or operator == 'Power' or operator == 'power' or operator == 'Pow' or operator == 'pow':
    print(first ** second)
else:
    print("Please enter a valid operator!")