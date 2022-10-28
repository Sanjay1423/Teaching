# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers separated by '#' representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

# Input Format
# 31#8#2019

# Constraints
# The given dates are valid dates between the years 1971 and 2100

# Output Format
# Saturday


from calendar import MONDAY
import datetime

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

input = list(input().split('#'))  # => ['31', '8', '2019']

day = datetime.date(int(input[2]), int(input[1]),
                    int(input[0]))  # => 2019-08-31


print(days[day.weekday()])
