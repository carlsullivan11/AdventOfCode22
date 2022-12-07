from stackClass import stackClass

crates = []
crates_p2 = []
for i in range(9):
    crates.append(stackClass())
    crates_p2.append(stackClass())

lines = open('day5/input.txt', 'r')
lines = lines.readlines()

for i in range(8):
    letter = 1
    for j in range(len(lines[i])//4):
        #print(lines[7 - i][letter])
        if(not lines[7 - i][letter] == ' '):
            crates[j].push(lines[7 - i][letter])
            crates_p2[j].push(lines[7 - i][letter]) 
        letter += 4
        
for i in range(10, len(lines)):
    move = lines[i].split()
    num = int(move[1])
    frm = int(move[3]) - 1
    to = int(move[5]) - 1
    #print(i,': ', 'Amount: ',num, 'From: ',frm, 'To: ',to)
    for j in range(num):
        crates[to].push(crates[frm].pop())

    temp = []
    for j in range(num):
        temp.append(crates_p2[frm].pop())
    for j in range(num):
        crates_p2[to].push(temp.pop())

print('Part 1: ')
for i in range(9):
    print(crates[i].peek(), end='')
print()
print('Part 2: ')
for i in range(9):
    print(crates_p2[i].peek(), end='')

