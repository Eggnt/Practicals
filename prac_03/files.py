"""Asking for the user's name and writing to file"""
OUTPUT_FILE = 'name.txt'

user_name = input("Please enter your name:")

out_file = open(OUTPUT_FILE, 'w')
print(f"{user_name}", file=out_file)
out_file.close()

"""Opening the written file and telling the user their name"""

INPUT_FILE = 'name.txt'

infile = open(INPUT_FILE, 'r')
name = infile.readline()
print(f"Your name is {name}")
infile.close()

"""Reading numbers.txt and adding finding the sum of the first two lines"""

NUMBER_INPUT_FILE = 'numbers.txt'

num_infile = open(NUMBER_INPUT_FILE, 'r')

sum_two = int(num_infile.readline()) + int(num_infile.readline())
print(sum_two)
num_infile.close()

"""Reading a file and finding the sum of all lines"""

NUMBER_INPUT_FILE = 'numbers.txt'

cumulative_total = 0

num_infile = open(NUMBER_INPUT_FILE, 'r')

for line in num_infile:
    cumulative_total += int(line)
print(cumulative_total)
