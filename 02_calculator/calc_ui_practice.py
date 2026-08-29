from calc_logic_practice import add, subtract, multi, divis

def calculation(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Try again...")


def main():
    while True:
        print("\nCalculator")
        print("1. - Add; 2. - Subtraction; 3. - Multiplication; 4. - Division; 5. - Exit.")

        choice = input("Choose a number from the list: ").strip()

        if choice == "5":
            print("Se ya...")
            break

        if choice in ("1", "2", "3", "4"):
            a = calculation("Write a first number: ")
            b = calculation("Write a second number: ")

            try:
                if choice == "1":
                    print(f"Result - '{add(a, b)}'")
                elif choice == "2":
                    print(f"Result - '{subtract(a, b)}'")
                elif choice == "3":
                    print(f"Result - '{multi(a, b)}'")
                elif choice == "4":
                    print(f"Result - '{divis(a, b)}'")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        else:
            print("Error: Try again...")

if __name__ == "__main__":
    main()

