def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount


def main():
    print("=== Simple Interest Calculator ===")

    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    interest, total_amount = calculate_simple_interest(principal, rate, time)

    print("\n--- Results ---")
    print(f"Principal Amount: {principal:.2f}")
    print(f"Interest Rate: {rate:.2f}%")
    print(f"Time Period: {time:.2f} years")
    print(f"Simple Interest: {interest:.2f}")
    print(f"Total Amount: {total_amount:.2f}")


if __name__ == "__main__":
    main()
