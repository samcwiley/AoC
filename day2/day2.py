with open('inputs2.txt') as f:
	lines = [line.rstrip() for line in f] #gets inputs and puts in array

# This scoring matrix assigns points based on your play (X, Y, Z) and opponent's play (A, B, C)
# each correlate to (Rock, Paper, Scissors). Score = (0,3,6) for (loss, draw, win) + (1,2,3) for (R, P, S)
#_|_X_Y_Z
#A| 4 8 3
#B| 1 5 9
#C| 7 2 6
score = [[4,8,3],[1,5,9],[7,2,6]] 
opp = {"A" : 0, "B" : 1, "C" : 2} #Assigns numbers to each throw to be able to call winLoss matrix for points
me = { "X" : 0, "Y" : 1, "Z" : 2}


totalPoints = 0
for line in lines:  #go through each line
	oppThrow = opp.get(line.split()[0]) #takes line of input and converts it into (0,1,2) for opponent's and my throws
	myThrow = me.get(line.split()[1])
	roundPoints = score[oppThrow][myThrow] #finds points won this round based on mine and opponent's throws
	totalPoints += roundPoints
print("The total score of all of the rounds given the cheat sheet is: " + str(totalPoints) + " points")

#PART TWO: (X,Y,Z) now tells (loss, draw, win)
#rpsMatrix to determine (R,P,S) throw necessary for (X,Y,Z) outcome given (A,B,C) opponent throw
#_|_X_Y_Z_
#A| S R P
#B| R P S
#C| P S R
rpsMatrix = [['S','R','P'],['R','P','S'],['P','S','R']]
out = {"X":0, "Y":1, "Z":2} #now (X,Y,Z) represent outcome (Loss, Draw, Win), still represented as (0, 1, 2)
rps = {"R":0, "P":1, "S":2} #converts the needed throw into a number to find score

totalPoints = 0
for line in lines:
	oppThrow = opp.get(line.split()[0]) #convert opponent throw and outcome into (0,1,2)
	outcome = out.get(line.split()[1])
	neededThrow = rpsMatrix[oppThrow][outcome] #gets required (R,P,S) to account for opp throw and outcome
	myThrow = rps.get(neededThrow) #converts needed throw into number
	roundPoints = score[oppThrow][myThrow] #finds score based on each throw, as above
	totalPoints += roundPoints
print("The total score of all rounds if (X,Y,Z) represents (Loss, Draw, Win) is: " + str(totalPoints) + " points")
