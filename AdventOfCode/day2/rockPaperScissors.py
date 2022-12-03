score = 0

opponent = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
myHand = {'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}
myScore = {'X':1, 'Y':2, 'Z':3}

lines = open('input.txt', 'r')
lines = lines.readlines()

for round in lines:
    if(round[0] == 'A' and round[2] == 'Y'):
        score += (6 + myScore.get(round[2]))
    elif(round[0] == 'B' and round[2] == 'Z'):
        score += (6 + myScore.get(round[2]))
    elif(round[0] == 'C' and round[2] == 'X'):
        score += (6 + myScore.get(round[2]))
    elif(opponent.get(round[0]) == myHand.get(round[2])):
        score += (3 + myScore.get(round[2]))
    else:
        score += myScore.get(round[2])

print(score)

opp = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']
score = 0

for round in lines:
    opponentHand = round[0]
    if(round[2] == 'X'):
        score += myScore.get(me[opp.index(opponentHand) - 1])
    elif(round[2] == 'Y'):
        score += (3 + myScore.get(me[opp.index(opponentHand)]))
    else:
        if(opp.index(opponentHand) == 2):
            score += (6 + myScore.get(me[0]))
        else:
            score += (6 + myScore.get(me[opp.index(opponentHand) + 1]))
        

print(score)
