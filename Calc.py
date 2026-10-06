print("How are you doing? I hope you re doing great!")

name = (input("What's your name: "))
OPERATION = ["add", "subtract", "multiply", "divide"]


def get_number():
    while True:
        try:
            while True:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                if ValueError:
                    print("Invalid Value")
                break
            print("\nAvailable Operations:")
            for operate in OPERATION:
                print("-", operate)

            while True:
                operator = input("Operation: ").strip().lower()

                if operator not in OPERATION:
                    print("Invalid operation.")
                    
                break
        except ValueError:
            print("Invalid Input! Please enter a valid number")
        return number1, number2, operator 


def calculate(number1, number2, operator):
        if operator == "add":
            return number1 + number2
        elif operator == "subtract":
            return number1 - number2
        elif operator == "multiply":
            return number1 * number2
        if operator == "divide":
            if number2 == 0:
                return "Cannot divide by zero."
            else:
                return number1 / number2

        

def main():
    
    while True:
        number1, number2, operator = get_number()
        print(f"{name}, you've entered:")
        print(f"First Number : {number1}")
        print(f"Second Number: {number2}")
        print(f"Operation    : {operator}")
        result = calculate(number1, number2, operator)
        print(f"Result = {result}")
        ask = input("Do you want another calculation? (yes/no): ").strip().lower()
        if ask == "yes":
            continue

        elif ask == "no":
            print("Thank you for using the calculator!")
            break
        else:
            print("Please enter yes or no.")

main()
