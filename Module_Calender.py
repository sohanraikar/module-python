import calendar  

def display_month(year, month):  
    """Display the calendar for a specific month in a given year."""  
    print(calendar.month(year, month))  

def display_year(year):  
    """Display the calendar for the entire year."""  
    print(calendar.calendar(year))  

def is_leap_year(year):  
    """Check if a given year is a leap year."""  
    return calendar.isleap(year)  

def main():  
    """Main function to run the calendar module."""  
    while True:  
        print("\nWelcome to the Calendar Module!")  
        print("1. Display a month's calendar")  
        print("2. Display a year's calendar")  
        print("3. Check if a year is a leap year")  
        print("4. Exit")  
        
        choice = input("Please enter your choice (1-4): ")  
        
        if choice == '1':  
            year = int(input("Enter year (e.g., 2022): "))  
            month = int(input("Enter month (1-12): "))  
            display_month(year, month)  
        
        elif choice == '2':  
            year = int(input("Enter year (e.g., 2022): "))  
            display_year(year)  
        
        elif choice == '3':  
            year = int(input("Enter year (e.g., 2022): "))  
            if is_leap_year(year):  
                print(f"{year} is a leap year.")  
            else:  
                print(f"{year} is not a leap year.")  
        
        elif choice == '4':  
            print("Exiting the Calendar Module. Goodbye!")  
            break  
        
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()