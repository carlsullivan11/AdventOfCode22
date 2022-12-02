elf = 1
maxCalories = 0
maxElf = 0

file = open('input.txt')
lines = file.readlines()

calCount = 0
calList = []
for cal in lines:
    if(not cal == '\n'):
        calCount += int(cal)
    else:
        calList.append(calCount)
        elf += 1
        calCount = 0

print('Elf: ', elf, 'CalCount: ', max(calList))
calList.sort(reverse=True)

print('Top 3 total: ', calList[0] + calList[1] + calList[2])
        