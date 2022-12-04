#Prompt: https://adventofcode.com/2022/day/3
#Inputs: https://adventofcode.com/2022/day/3/input

total = 0
with open('inputs3.txt') as f: (total += (ord([value for value in list(line[0:len(line)//2]) if value in list(line[len(line)//2:])][0]) - 38 if 65 <= ord([value for value in list(line[0:len(line)//2]) if value in list(line[len(line)//2:])][0]) <= 90 else ord([value for value in list(line[0:len(line)//2]) if value in list(line[len(line)//2:])][0]) -96)) for line in f
#	lines = [line.rstrip() for line in f]
#total = 0
#for line in lines:
#    compartment1, compartment2 = line[0:len(line)//2], line[len(line)//2:]
#    common = [value for value in list(compartment1) if value in list(compartment2)]
#    total += (ord(common[0]) - 38 if 65 <= ord(common[0]) <= 90 else ord(common[0]) -96)
#print("Sum of priorities for individual elve's rucksacks: " + str(total) + " points.")
print(total)

#total = 0
#for i in range(2,len(lines)):
#i = 2
#while i < len(lines):
#    common = [value for value in list(lines[i-2]) if value in list(lines[i-1]) and value in list(lines[i])]
#    print(common)
#    i += 3
#    total += (ord(common[0]) - 38 if 65 <= ord(common[0]) <= 90 else ord(common[0]) -96)
#print("Sum of priorities for rucksacks in groups of 3 elves: " + str (total) + " points.")