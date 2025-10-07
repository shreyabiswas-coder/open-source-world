def check_even_odd(number):
    """Check if a number is even or odd and return the result."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    print("=== Even or Odd Checker ===")
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
