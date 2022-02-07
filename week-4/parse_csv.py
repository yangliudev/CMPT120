import os
import pathlib

# Debug path
print('DOES FILE EXIST?', os.path.exists(r'/Users/yangliu/Desktop/SFU/CMPT_120/week-4/data.csv'))
print('Current working directory', pathlib.Path().resolve())
print('Directory of script being run', pathlib.Path(__file__).parent.resolve())

# Read file
file = open("/Users/yangliu/Desktop/SFU/CMPT_120/week-4/data.csv")

for line in file:
    print(line)