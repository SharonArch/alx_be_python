from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()   # save current datetime
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date


def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)  # save future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
