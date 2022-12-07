#this is very janky please do not read
import numpy as np
with open('inputs5.txt') as f:
	lines = [line.rstrip() for line in f]

stacks = []
for line in lines:
    if '[' in line:
        stacks.append([line[i] for i in range(1, len(line), 4)]) #makes list of package letters or blank spaces
    elif len(line) == 0:
        length = max(map(len, stacks))
        y = np.array([i+[' ']*(length-len(i)) for i in stacks]) #converts list to numpy array with padding to make square
        y = np.rot90(y, 3).tolist() #rotates the array 270 degrees and casts back to list
        stacks = [list(filter(lambda x: x!= ' ', row)) for row in y] #removes blank items to make ragged list of lists
        stacks2 = stacks
    elif 'move' in line:
        [amount, source, dest] = line.split()[1:len(line.split()):2]
        #for i in range(int(amount)):
        #    stacks[int(dest)-1].append(stacks[int(source)-1].pop())
        stacks2[int(dest)-1] = stacks2[int(dest)-1] + stacks2[int(source)-1][-int(amount):]
        stacks2[int(source)-1] = stacks2[int(source)-1][:-int(amount)]
#print(''.join([stack[-1] for stack in stacks]))
print(''.join([stack[-1] for stack in stacks2]))
