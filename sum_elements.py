# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def get_number_of_elements():
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print("Invalid input. Please provide a number from 1 to 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    arr = []
    print(f"Enter {n} integers:")
    while len(arr) < n:
        try:
            num = int(input(f"Element {len(arr)+1}: "))
            arr.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return arr

def main():
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
