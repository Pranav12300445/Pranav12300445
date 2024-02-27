import cmath

try:
    mode = int(input("1 FOR NORMAL AND 2 FOR SCIENTIFIC MODE "))

    if mode == 1:
        num = float(input("Enter no. : "))

        while True:

            opt = str(input("Enter the operation you want to perform: "))

            if opt == '=':
                break
            num1 = float(input("Enter no. : "))

            if opt == '+':
                num += num1
            elif opt == '-':
                num -= num1
            elif opt == '*':
                num *= num1
            elif opt == '/':
                num /= num1
            elif opt == '%':
                num %= num1
            else:
                print("Invalid input")
        print(num)

    elif mode == 2:
        num2 = float(input("Enter no. : "))

        opt1 = str(input("Enter the operation you want to perform: "))

        if opt1 == '√' or opt1 == 'sqrt':
            num2 = cmath.sqrt(num2)
        elif opt1 == 'Sin' or opt1 == 'sin':
            num2 = cmath.sin(num2)
        elif opt1 == 'Cos' or opt1 == 'cos':
            num2 = cmath.cos(num2)
        elif opt1 == 'Tan' or opt1 == 'tan':
            num2 = cmath.tan(num2)
        elif opt1 == 'Sin^-1' or opt1 == 'sin^-1':
            num2 = cmath.asin(num2)
        elif opt1 == 'Cos^-1' or opt1 == 'cos^-1':
            num2 = cmath.acos(num2)
        elif opt1 == 'Tan^-1' or opt1 == 'tan^-1':
            num2 = cmath.atan(num2)
        else:
            print('Invalid input')
        print(num2)

    else:
        print("Invalid mode selection. Choose 1 or 2.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")
