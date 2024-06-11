import calendar

# Function to print the calendar of a given month and year
def print_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Print the calendar for the specified month and year
    print(cal.formatmonth(year, month))

# Example usage
year = 2050
month = 9
print_calendar(year, month)
