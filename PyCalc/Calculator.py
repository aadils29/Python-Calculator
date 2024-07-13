num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
op = input("Operaton: ")

if op == "+":
    print(num1 + num2)
elif op == "-" :
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Input valid operation")
