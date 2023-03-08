num1 = int(input())
op = input()
num2 = int(input())

if not (-100 <= num1 <= 100) or not (-100 <= num2 <= 100):
    print("Input values must be between -100 and 100.")
else:
    if op == "+":
        result = num1 + num2
    elif op == "*":
        result = num1 * num2

    print(result)
