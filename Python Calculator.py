def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()

"""
hi you forgot to make the file a .py btw, and the code is already good. if you'd like to really complete it, remember to add input validation (print back a message to the user that the operation works 
or show them what is happeing) and error handling (making sure there is an error message when the user inputs incorrect numbers/strings) for example, when i input a number when the code asks for only yes or no
the code crashes, or when i input a string when i should input a number, the code crashes. instead of allowing the code to crash during unexpected input, try to expect the worst input from the user so you have
it covered. overally still good and basic :D
"""
