import calendar

def display_calendar():
    
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    cal = calendar.TextCalendar(calendar.SUNDAY)

    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

display_calendar()