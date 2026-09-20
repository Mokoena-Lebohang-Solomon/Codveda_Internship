import sys
print("========================================================================")
print("|                     Basic Calculator                                 |")
print("========================================================================\n")
print("To use the calculator, Please enter two number \n")
def get_Input(sMessage: str, sErrorMessage: str) :
    while True:
        try:
            intInput_Choose: int = int(input(sMessage))
            return intInput_Choose

        except ValueError:
            print(sErrorMessage)


intFirstNumber:int = get_Input("Enter first number:", "Please enter a valid number.")
intSecondNumber:int = get_Input("Enter second number:\n","Please enter a valid number.")

print("........................................................................")
print("Instructions for calculator:" )
print("Press 1 to Add two numbers." )
print("Press 2 to Multiply two numbers.")
print("Press 3 to Divide two numbers.")
print("Press 4 to Subtract  two numbers.")
print("Press 5 to Close calculator.")
print("........................................................................\n")

intInput_Choose: int = get_Input("Enter your choice: ","Invalid choice. Please enter a number.")
def addTwoNumbers(intFirstNumber:int, intSecondNumber:int):
    return intFirstNumber + intSecondNumber

def multiplyTwoNumbers(intFirstNumber:int, intSecondNumber:int):
    return intFirstNumber * intSecondNumber

def divideTwoNumbers(intFirstNumber:int, intSecondNumber:int):
    while True:
     try:
         intTotal:int = intFirstNumber / intSecondNumber
         return intTotal

     except ZeroDivisionError:
        print("you can't divide by zero")
        intSecondNumber:int = get_Input("Enter second number:\n","Please enter a valid number.")

def subtractTwoNumbers(intFirstNumber:int, intSecondNumber:int):
    return intFirstNumber - intSecondNumber


match intInput_Choose:
    case 1:
           print(f"Sum of the {intFirstNumber} and {intSecondNumber} is { addTwoNumbers(intFirstNumber,intSecondNumber)}")

    case 2:
       print(f"Product of {intFirstNumber} and {intSecondNumber} is {multiplyTwoNumbers(intFirstNumber,intSecondNumber)}")

    case 3:
         print(f"Division of {intFirstNumber} and {intSecondNumber} is {divideTwoNumbers(intFirstNumber,intSecondNumber)}")

    case 4:
        print(f"Difference of {intFirstNumber} and {intSecondNumber} is {subtractTwoNumbers(intFirstNumber,intSecondNumber)}")

    case 5:
        print("Closing calculator...")
        sys.exit()

    case _:
        print("Invalid input")







