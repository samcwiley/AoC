#Prompt: https://adventofcode.com/2022/day/3
#Inputs: https://adventofcode.com/2022/day/3/input

with open('inputs3.txt') as f:
	lines = [line.rstrip() for line in f]
total = 0
for line in lines:
    compartment1, compartment2 = line[0:len(line)//2], line[len(line)//2:]
    common = [value for value in list(compartment1) if value in list(compartment2)]
    total += (ord(common[0]) - 38 if 65 <= ord(common[0]) <= 90 else ord(common[0]) -96)
print("Sum of priorities for individual elve's rucksacks: " + str(total) + " points.")

total = 0
for i in range(2, len(lines), 3):
    common = [value for value in list(lines[i-2]) if value in list(lines[i-1]) and value in list(lines[i])]
    #i += 3
    total += (ord(common[0]) - 38 if 65 <= ord(common[0]) <= 90 else ord(common[0]) -96)
print("Sum of priorities for rucksacks in groups of 3 elves: " + str (total) + " points.")