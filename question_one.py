def get_input():
    while True:
        try:
            input_string = input("Enter a list of integers separated by spaces: ")
            numbers = list(map(int, input_string.split()))
            return numbers
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")

def process_numbers(numbers):
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers

def display_result(sorted_numbers):
    print("\nThe final answer is:")
    print(sorted_numbers)

def main():
    numbers = get_input()
    sorted_numbers = process_numbers(numbers)
    display_result(sorted_numbers)

if __name__ == "__main__":
    main()
