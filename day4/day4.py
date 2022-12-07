with open('inputs4.txt') as f:
    lines = [line.rstrip() for line in f]
total1, total2 = 0, 0
for line in lines:
    [one, two] = line.split(',')
    [s1, e1] = [int(i) for i in one.split('-')]
    [s2, e2] = [int(i) for i in two.split('-')]
    total1 += (0,1)[(s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)]
    total2 += (0,1)[s2 in range(s1,e1+1) or s1 in range(s2, e2+1)]
print(f"There are {total1} total rows where one elf's assignments encompass their partner's.")
print(f"There are {total2} rows where the two elves' assignments overlap at all.")