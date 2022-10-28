# Reformat Date

# Given a date string in the form Day Month Year, where:

# => Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}. =>
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}. =>
# Year is in the range [1900, 2100]. Convert the date string to the format YYYY-MM-DD, where:=>
# YYYY denotes the 4 digit year. =>MM denotes the 2 digit month. =>DD denotes the 2 digit day.

# Input Format
# 20th Oct 2052

# Constraints
# The given dates are guaranteed to be valid, so no error handling is necessary.

# Output Format
# 2052-10-20


import datetime

input = list(input().split(' '))   # => ['20th', 'Oct', '2052']


date = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5, '6th': 6, '7th': 7, '8th': 8, '9th': 9, '10th': 10,
        '11th': 11, '12th': 12, '13th': 13, '14th': 14, '15th': 15, '16th': 16, '17th': 17, '18th': 18, '19th': 19, '20th': 20,
        '21st': 21, '22nd': 12, '23rd': 13, '24th': 24, '25th': 25, '26th': 26, '27th': 27, '28th': 28, '29th': 29, '30th': 30, '31st': 31}

months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


print(datetime.date(int(input[2]), months[input[1]], date[input[0]]))
