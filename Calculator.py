
def addition(num1,num2):
    total = num1 + num2
    print("The addition of ",num1," and ",num2," is ",total)
def subtraction(num1,num2):
    total = num1 - num2
    print("The subtraction of ", num1," and ",num2," is ",total)
def multiplication(num1,num2):
    total = num1 * num2
    print("The Multiplication of ",num1," and ",num2," is ",total)
def division(num1,num2):
    total = num1 / num2
    print("The Division of ",num1," and ",num2," is ",total)
def modulo(num1,num2):
    total = num1 % num2
    print("The Modulo of ",num1," and",num2," is ",total)
def main():
    while True:
        txt = "Basic Calculator"
        message = txt. center(50)
        print(message)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("q. Quit")

        choice = input(">")

        if choice == "1":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            addition(num1,num2)
        elif choice == "2":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            subtraction(num1,num2)
        elif choice == "3":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            multiplication(num1,num2)
        elif choice == "4":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            division(num1,num2)
        elif choice == "5":
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            modulo(num1,num2)
        elif choice == "q":
            break
        else:
            print("Invalid Choice, Please try again!")
main()
