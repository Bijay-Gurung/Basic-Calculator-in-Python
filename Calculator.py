class Calculator:
    def addition(self,num1,num2):
        total = num1 + num2
        print(total)
    def subtractioin(self,num1,num2):
        total = num1 - num2
        print(total)
    def multiplication(self,num1,num2):
        total = num1 * num2
        print(total)
    def division(self,num1,num2):
        if num2 != 0:
            total = num1 / num2
            print(total)
        else:
            print(f"{num1} cannot divided by 0!")

    def main(self):
        while True:
            title = "Basic Calculator".center(50)
            print(title)
            num1 = int(input("Enter first Number: "))
            num2 = int(input("Enter Second Number: "))

            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("q. Quit")
            choice = input(">")

            if choice == "1":
                self.addition(num1,num2)
            elif choice == "2":
                self.subtractioin(num1,num2)
            elif choice == "3":
                self.multiplication(num1,num2)
            elif choice == "4":
                self.division(num1,num2)
            elif choice == "q" or choice == "Q":
                break
            else:
                print("Invalid input, try again!")

if __name__ == "__main__":
    basicCalculator = Calculator()
    basicCalculator.main()