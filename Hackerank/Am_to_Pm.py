#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Split the input string into hours, minutes, seconds, and AM/PM parts
    time_parts = s.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = time_parts[2][:2]  # Extract the first 2 characters for seconds
    am_pm = time_parts[2][-2:]  # Extract the last 2 characters for AM/PM

    # Check if it's PM and not 12 PM
    if am_pm == 'PM' and hours != 12:
        hours += 12
    # Check if it's AM and 12 AM
    elif am_pm == 'AM' and hours == 12:
        hours = 0

    # Format the hours as a 2-digit string and create the 24-hour time string
    military_time = f"{hours:02d}:{minutes:02d}:{seconds}"

    return military_time

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)


