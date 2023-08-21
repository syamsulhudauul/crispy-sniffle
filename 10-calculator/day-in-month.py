def is_leap(year):
    """Check if year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # Divisible by 4, 100, and 400
                return True
            else:
                # Divisible by 4 and 100, but not 400
                return False
        else:
            # Divisible by 4, but not 100
            return True
    else:
        # Not divisible by 4
        return False
    
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 
              31, 30, 31]
def days_in_month(year, month):
    """Return the number of days in a month"""
    if month > 12 or month < 1:
        return "Invalid month"
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
