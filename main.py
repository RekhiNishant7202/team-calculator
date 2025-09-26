from calculator import add, subtract, multiply, divide
from advanced import sqrt, power, percentage

def print_menu():
    print("Team Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Square root")
    print("6) Power")
    print("7) Percentage")
    print("0) Exit")

def input_two_numbers(prompt1="Enter first number: ", prompt2="Enter second number: "):
    a = float(input(prompt1))
    b = float(input(prompt2))
    return a, b

def main():
    while True:
        print_menu()
        choice = input("Choose option: ").strip()
        try:
            if choice == "1":
                a, b = input_two_numbers()
                print("Result:", add(a, b))
            elif choice == "2":
                a, b = input_two_numbers()
                print("Result:", subtract(a, b))
            elif choice == "3":
                a, b = input_two_numbers()
                print("Result:", multiply(a, b))
            elif choice == "4":
                a, b = input_two_numbers()
                print("Result:", divide(a, b))
            elif choice == "5":
                x = float(input("Enter number: "))
                print("Result:", sqrt(x))
            elif choice == "6":
                base = float(input("Enter base: "))
                exp = float(input("Enter exponent: "))
                print("Result:", power(base, exp))
            elif choice == "7":
                part = float(input("Enter part: "))
                whole = float(input("Enter whole: "))
                print(f"Result: {percentage(part, whole)}%")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()