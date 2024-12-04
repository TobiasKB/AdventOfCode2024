from contextlib import nullcontext

import pandas as pd
import numpy as np
#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.
#
# Dimensionality: Changes all the time, it could be a infinite version
# Pseudocode:#

input_file = "/Users/tobiashome/Library/CloudStorage/GoogleDrive-t.kraftblank@gmail.com/My Drive/25_Sonstiges/Programmieren/AdventOfCode2024/input2ndAdvent.txt"

# Open the file for reading
with open(input_file, "r") as file:
    for line in file:
        # Split the line into a list of integers (remove newline and split by spaces)
        numbers = list(map(int, line.strip().split()))


# Read it so its compatible with pandas
with open(input_file, "r") as file:
    data = [list(map(int, line.strip().split())) for line in file]

# Convert to a DataFrame, filling missing values with NaN
safeCount = 0
df = pd.DataFrame(data)

flag_increase = False
flag_decrease = False

for index, row in df.iterrows():
    # Drop NaN values and convert to a list for valid comparisons
    valid_row = row.dropna().tolist()
    # Only proceed if the row has at least two numbers
    if len(valid_row) > 1:
        flag_increase = False
        flag_decrease = False
        for col in range(len(valid_row) - 1):

            diff = valid_row[col + 1] - valid_row[col]

            if (flag_increase and  flag_decrease ) or abs(diff)>2:
                #print("unsafe")
                break

            if valid_row[col] < valid_row[col + 1] :
                flag_decrease = True
            elif valid_row[col] > valid_row[col + 1] :
                flag_increase = True
        else:#this else block triggers when the for loop is run without any break points.
            safeCount += 1

print(f"Safe count: {safeCount}")


