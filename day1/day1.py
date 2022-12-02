with open('inputs_day1.txt') as f:
	lines = [line.rstrip() for line in f]

elfTotal = 0
maxCal = 0

for line in lines:
	if line == '':
		if elfTotal > maxCal:
			maxCal = elfTotal
		elfTotal = 0
	else:
		elfTotal = elfTotal + int(line)
print("The elf with the greatest amount of calories had: " + str(maxCal) + " Calories")

elfTotals = []
subtotal = 0
for line in lines:
	if line == "":
		elfTotals.append(subtotal)
		subtotal = 0
	else:
		subtotal = subtotal + int(line)

elfTotals = sorted(elfTotals, key=int, reverse=True)
print("The top 3 elves had: " + str(sum(elfTotals[0:3])) + " Calories")
