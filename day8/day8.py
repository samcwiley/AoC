import numpy as np
exampleInput = '''30373
25512
65332
33549
35390'''

lines = exampleInput.split('\n')
treeMap = [list(line) for line in lines]
visibleMap = [[0]*len(treeMap[0])]*len(treeMap)
#Check from top first:
#print(f'X max is {len(treeMap[0])}, ymax is {len(treeMap)}')
print(visibleMap)
for x in range(1,len(treeMap[0])-1):
    for y in range(1,len(treeMap)-1):
        if int(treeMap[y][x]) > int(treeMap[y-1][x]):
            print(f'{treeMap[y][x]}>{treeMap[y-1][x]}, adding 1 to point {y},{x}')
            visibleMap[y][x] = 1
            print(visibleMap)
print(visibleMap)