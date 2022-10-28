# Number of Days Between Two Dates 1

# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

# Input Format
# 2019-06-29#2019-06-30

# Constraints
# The given dates are valid dates between the years 1971 and 2100.

# Output Format
# 1


import datetime

input = list(input().split('#'))  # => ['2019-06-29', '2019-06-30']


day1 = datetime.datetime.strptime(
    input[0], "%Y-%m-%d")  # =>  2019-06-29 00:00:00
print(day1)

day2 = datetime.datetime.strptime(
    input[1], "%Y-%m-%d")  # =>  2019-06-30 00:00:00

day = day2 - day1   # => 1 day, 0:00:00


print(abs(day.days))
