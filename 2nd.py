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

print(df.shape)
# for index, row in df.iterrows():
#     for col in range(len(row) - 1):  # Iterate through columns, avoiding index out of range
#         if row[col] != row[col + 1]:  # Combine conditions with !=
#             if abs(row[col] - row[col + 1]) > 2:
#                 print("Unsafe")
#             else:
#                 print("Safe")
#                 safeCount += 1
#         else:
#            print("Unsafe")

# for index, row in df.iterrows():
#     for col in range(len(row) - 1):
#         # Skip if either value is NaN
#         if pd.notna(row[col]) and pd.notna(row[col + 1]):
#             if row[col] != row[col + 1] and abs(row[col] - row[col + 1]) <= 2:
#                 safeCount += 1
import pandas as pd

flag_increase = False
flag_decrease = False

for index, row in df.iterrows():
    # Drop NaN values and convert to a list for valid comparisons
    valid_row = row.dropna().tolist()
    print(valid_row)
    # Only proceed if the row has at least two numbers
    if len(valid_row) > 1:
        flag_increase = False
        flag_decrease = False
        for col in range(len(valid_row) - 1):

            if flag_increase == True and  flag_decrease == True:
                print("unsafe")
                continue
            if  abs(valid_row[col] - valid_row[col + 1]) > 2:
                print("unsafe")
                continue
            if valid_row[col] < valid_row[col + 1] :
                flag_decrease = True
            elif valid_row[col] > valid_row[col + 1] :
                flag_increase = True
            else:
                safeCount += 1

print(f"Safe count: {safeCount}")


#ChatGPT Version
safeCount = 0

for _, row in df.iterrows():
    valid_row = row.dropna().tolist()
    if len(valid_row) > 1:
        flag_increase, flag_decrease = False, False

        for col in range(len(valid_row) - 1):
            diff = valid_row[col + 1] - valid_row[col]

            if abs(diff) > 2 or (flag_increase and flag_decrease):
                print("unsafe")
                break

            if diff > 0:
                flag_increase = True
            elif diff < 0:
                flag_decrease = True
        else:
            safeCount += 1  # Only increment if the loop completes without break

print(f"Safe count: {safeCount}")

