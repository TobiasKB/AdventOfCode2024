import pandas as pd

#Vanilla Python
input_file = "/Users/tobiashome/Library/CloudStorage/GoogleDrive-t.kraftblank@gmail.com/My Drive/25_Sonstiges/Programmieren/AdventOfCode2024/input_1stAdvent.txt"
# File path

with open(input_file, 'r') as file:
    lines = file.readlines()

# Process each line by splitting on whitespace and converting to integers
data = [list(map(int, line.strip().split())) for line in lines]

# Extract columns
column1 = [row[0] for row in data]
column2 = [row[1] for row in data]

#Pandas python
data = pd.read_csv(input_file,header=None,sep=r'\s+')
column1 = data[0].tolist()
column2 = data[1].tolist()

column1.sort()
column2.sort()

listDistance = 0

for i in range(len(column1)):
        listDistance += abs(column1[i] - column2[i])

print(listDistance)
##Part2
newDistance = 0
for item in column1:
    countitem = column2.count(item)
    newDistance += item*countitem

print(newDistance)