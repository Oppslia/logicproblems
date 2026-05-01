def Day_1():
    password = 0
    position = 50
    with open("Advent2025Resources/day_1_input.txt") as file:
        for fLine in file:
            line = int(fLine[1:])
            if fLine[0] == 'R':
                position = (position + line) % 100
            else:
                if (position - (line % 100)) < 0:
                    position = (position - (line % 100)) + 100    
                else:
                    position = position - (line % 100)
            if position == 0:
                password += 1
    return password
def Day_1_pt_2():
    password = 0
    position = 50
    with open("Advent2025Resources/day_1_input.txt") as file:
        for fLine in file:
            line = int(fLine[1:])
            if fLine[0] == 'R':
                password += (position + line) // 100
                position = (position + line) % 100
            else:
                if (position - (line % 100)) < 0:
                    if position == 0:
                        password += (line // 100)
                    else:
                        password += ((100 - position) + (line)) // 100 
                    position = (position - (line % 100)) + 100    
                else:
                    password += (line // 100)
                    position = position - (line % 100)
                    if position == 0 and (line % 100) != 0 : # position = 0 and line = 100:
                        password += 1
    return password
def Day_2_pt_1():
    total = 0
    with open("Advent2025Resources/day_2_input.txt") as file:
        for ranges in file.read().split(','):
            seperatedRanges = ranges.split('-')
            for i in range(int(seperatedRanges[0]), int(seperatedRanges[1])):
                if len(str(i)) % 2 == 0:
                    if (s := str(i))[:len(s) // 2] == s[len(s) // 2:]: # Check if the first half equals the second half
                        total += i
    return total

def Day_2_pt_2():
    def getDivisors(num):
        divs:set = {1} # exclude 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divs.add(i)
                divs.add(num // i)
        return divs
    total = 0
    with open("Advent2025Resources/day_2_input.txt") as file:
        for ranges in file.read().split(','):
            seperatedRanges = ranges.split('-')
            for b in range(int(seperatedRanges[0]), int(seperatedRanges[1]) + 1):
                if(len(str(b)) < 2):
                    continue
                patternLengths = getDivisors(len(str(b)))
                b = str(b)
                patternExists = False
                for pLength in patternLengths:
                    pattern = b[:pLength]
                    patternDetected = False
                    for i in range(0, len(b), pLength):
                        numSlice = b[i:i + pLength]
                        if numSlice != pattern:
                            patternDetected = False
                            break
                        else:
                            patternDetected = True
                    if patternDetected:
                        patternExists = True
                if patternExists:
                    total += int(b)        
    return total

def Day_3_pt_1():
    with open("Advent2025Resources/day_3_input.txt") as file:
        maximumJoltage = 0
        for bankNumber, bank in enumerate(file):
            bank = list(bank.strip())
            highestLeftIndex = 0
            for index in range(len(bank) - 1):
                if bank[index] > bank[highestLeftIndex] and index < len(bank) - 1:
                    highestLeftIndex = index
                    if bank[highestLeftIndex] == 9:
                        break
            highestRightIndex = highestLeftIndex + 1 # also first right index initially
            for rightIndex in range(highestLeftIndex + 1, len(bank)):
                if bank[rightIndex] > bank[highestRightIndex]:
                    highestRightIndex = rightIndex
                    if bank[highestRightIndex] == 9:
                        break
            print(f"Bank#{bankNumber} {bank[highestLeftIndex]}{bank[highestRightIndex]} bank Length = {len(bank)}")
            print(f"Highest Left:{highestLeftIndex} : Highest Left Number:{bank[highestLeftIndex]} ")
            print(f"Highest Right:{highestRightIndex} : Highest Right Number:{bank[highestRightIndex]}\n {bank}")
            maximumJoltage += int(f"{bank[highestLeftIndex]}{bank[highestRightIndex]}")
    return maximumJoltage

def Day_3_pt_2():
    with open("Advent2025Resources/day_3_input.txt") as file:
        maximumJoltage = 0
        for bankNumber, batteryBank in enumerate(file):
            batteryBank = [int(x) for x in batteryBank.strip()]
            highestIndexes = {i: 0 for i in reversed(range(12))}
            startIndex = 0
            for storedBankKey, storedBankIndex in highestIndexes.items(): # get the 12
                loopLimitAllocation = len(batteryBank) - (storedBankKey + 1) # Set the end range for the current index
                if startIndex == loopLimitAllocation: #
                    print('hit')
                    highestIndexes[storedBankKey] = startIndex # Set index equal to the start
                    startIndex += 1
                    continue
                loopStart = startIndex + 1 # Set the beginning of the loop one place from the start
                print(f"New Range to search Indexes: {loopStart} - {loopLimitAllocation}")
                if loopStart == loopLimitAllocation: # If the loop only has one value to check, set the highest index to that value and move on to the next index
                    print('hit2')
                    highestIndexes[storedBankKey] = loopStart
                    startIndex = loopStart
                    continue
                highestIndexes[storedBankKey] = startIndex # Set index equal to the start
                #The loop always needs at least the highest Indexes key + 1 of values left.
                #for example if range(startIndex-bank.len - bankIndex + 1) so 0-100 - 12, then the range lands on 67. 67-100 - 11 
                for index in range(loopStart, loopLimitAllocation + 1): # Compare the index we set(last highest + 1) to the range we defined((last highest + 1) + 1 : to the end of the bank)
                    if batteryBank[index] > batteryBank[highestIndexes[storedBankKey]]:
                        highestIndexes[storedBankKey] = index
                        startIndex = index + 1 # Move the starting index to the curent inde and forward one if a new higher number is found for the next iteration.
                if loopStart - 1 == startIndex: # If the loop did not find a higher number, move the start index up by 1 to prevent an infinite loop
                    startIndex += 1
                print(f"Finished processing bankKey: {storedBankKey} and bankValue(index):{highestIndexes[storedBankKey]} Actual value: {batteryBank[highestIndexes[storedBankKey]]}")
                    
            print(f"Bank#{bankNumber}")
            highestIndexesPrint = ''
            highestBankValuesPrint = ''
            for storedBankKey, storedBankIndex in highestIndexes.items():
                highestIndexesPrint += f"Highest indexes: {storedBankKey}:{storedBankIndex} "
                highestBankValuesPrint += f"Highest indexes value: {batteryBank[storedBankIndex]} "
            print(highestIndexesPrint)
            print(highestBankValuesPrint)
            
            print(int("".join([str(batteryBank[y]) for x, y in highestIndexes.items()])))
            maximumJoltage += int("".join([str(batteryBank[y]) for x, y in highestIndexes.items()]))
    return maximumJoltage

def Day_3_pt_2_v2():
    with open("Advent2025Resources/day_3_input.txt") as file:
        maximumJoltage = 0
        for bankNumber, batteryBank in enumerate(file):
            batteryBank = [int(x) for x in batteryBank.strip()]
            highestIndexes = {i: 0 for i in reversed(range(12))}
            startIndex = 0
            for storedBankKey, storedBankIndex in highestIndexes.items(): # get the 12
                highestIndexes[storedBankKey] = startIndex
                loopLimitAllocation = len(batteryBank) - (storedBankKey + 1) # Set the end range for the current index
                loopStart = startIndex + 1 # Set the beginning of the loop one place from the start
                if loopStart == loopLimitAllocation: #
                    if batteryBank[loopStart] > batteryBank[startIndex]:
                        highestIndexes[storedBankKey] = loopStart 
                        startIndex = loopStart + 1
                    else:
                        highestIndexes[storedBankKey] = startIndex # Set index equal to the start if it's higher than the current value
                        startIndex += 1
                    continue

                for index in range(loopStart, loopLimitAllocation + 1): # Compare the index we set(last highest + 1) to the range we defined((last highest + 1) + 1 : to the end of the bank)
                    if batteryBank[index] > batteryBank[highestIndexes[storedBankKey]]:
                        highestIndexes[storedBankKey] = index
                        startIndex = index + 1# Move the starting index to the curent inde and forward one if a new higher number is found for the next iteration.
                if loopStart - 1 == startIndex: # If the loop did not find a higher number, move the start index up by 1 to prevent an infinite loop
                    highestIndexes[storedBankKey] = startIndex
                    startIndex += 1
                                    
            print(f"Bank#{bankNumber}")  
            print(int("".join([str(batteryBank[y]) for x, y in highestIndexes.items()])))
            maximumJoltage += int("".join([str(batteryBank[y]) for x, y in highestIndexes.items()]))
    return maximumJoltage


def Day_4_pt_1_dep(): # Live Mutation
    with open("Advent2025Resources/day_4_input_test.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
        rows = len(lines)
        cols = len(lines[0])

        def getAdjacent(positionToCheck, rowNumber):
            adjacentPositions = []
            for r in range(rowNumber - 1, rowNumber + 2):
                for c in range(positionToCheck - 1, positionToCheck + 2):

                    # Skip the center cell itself
                    if r == rowNumber and c == positionToCheck:
                        continue

                    # Boundary check
                    if 0 <= r < rows and 0 <= c < cols:
                        adjacentPositions.append(lines[r][c])
            return adjacentPositions
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] != '@':
                    continue

                adjs = len([pos for pos in getAdjacent(c, r) if pos == '@'])
                if adjs < 4:
                    lines[r] = lines[r][:c] + 'X' + lines[r][c + 1:]
        removed = 0
        for line in lines:
            for char in line:
                if char == 'X':
                    removed += 1
        return removed
def Day_4_pt_1(): # No mutation
    with open("Advent2025Resources/day_4_input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
        rows = len(lines)
        cols = len(lines[0])

        def getAdjacent(positionToCheck, rowNumber):
            adjacentPositions = []
            for r in range(rowNumber - 1, rowNumber + 2):
                for c in range(positionToCheck - 1, positionToCheck + 2):

                    # Skip the center cell itself
                    if r == rowNumber and c == positionToCheck:
                        continue

                    # Boundary check
                    if 0 <= r < rows and 0 <= c < cols:
                        adjacentPositions.append(lines[r][c])
            return adjacentPositions
        removed = 0
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] != '@':
                    continue

                adjs = len([pos for pos in getAdjacent(c, r) if pos == '@'])
                if adjs < 4:
                    removed += 1

        return removed
def Day_4_pt_2(): #Sequential? Mutation
    with open("Advent2025Resources/day_4_input.txt") as file:
        lines = [line.rstrip() for line in file.readlines()]
        rows = len(lines)
        cols = len(lines[0])

        def getAdjacent(positionToCheck, rowNumber):
            adjacentPositions = []
            for r in range(rowNumber - 1, rowNumber + 2):
                for c in range(positionToCheck - 1, positionToCheck + 2):

                    # Skip the center cell itself
                    if r == rowNumber and c == positionToCheck:
                        continue

                    # Boundary check
                    if 0 <= r < rows and 0 <= c < cols:
                        adjacentPositions.append(lines[r][c])
            return adjacentPositions
        rowsCanBeChanged = True
        mutatedGrid = [row[:] for row in lines] 
        while rowsCanBeChanged:
            removed = 0
            for r, v in enumerate(lines):
                for c in range(len(v)):
                    if v[c] != '@':
                        continue
                    adjs = len([pos for pos in getAdjacent(c, r) if pos == '@'])
                    if adjs < 4:
                        mutatedGrid[r] = mutatedGrid[r][:c] + 'X' + mutatedGrid[r][c + 1:]
                        removed += 1
            lines = mutatedGrid
            if removed == 0:
                rowsCanBeChanged = False
            
        removed = 0
        for line in lines:
            for char in line:
                if char == 'X':
                    removed += 1
        return removed

def Day_5_pt_1():
    with open("Advent2025Resources/day_5_input.txt") as file:
        lines = file.readlines()
        ranges = lines[0:[line for line in range(len(lines)) if lines[line] == '\n'][0]]
        for line in range(len(ranges)):
            ranges[line] = ranges[line].rstrip()
        ingredients = lines[len(ranges) + 1:]
        for line in range(len(ingredients)):
            ingredients[line] = ingredients[line].rstrip()
        freshIds = 0
        for i in ingredients:
            for r in ranges:
                start, end = r.split('-')
                if int(i) >= int(start) and int(i) <= int(end):
                    freshIds+= 1
                    break
        return freshIds

def Day_5_pt_2():
    with open("Advent2025Resources/day_5_input.txt") as file:
        lines = file.readlines()
        ranges = lines[0:[line for line in range(len(lines)) if lines[line] == '\n'][0]]
        for line in range(len(ranges)):
             ranges[line] = ranges[line].rstrip()
        ranges.sort(key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1])))
        combinedOverlappingRanges = [f"{ranges[0].split('-')[0]}-{ranges[0].split('-')[1]}"]
        # The range are sorted so we can just compare the current range to the last merged range and merge if they overlap or add to the list if they don't'
        # Since the range is sorted, only the most recently merged range can overlap with the current range, so we only need to compare to the last merged range instead of all merged ranges
        for i in range(1, len(ranges)):
            last = combinedOverlappingRanges[-1]
            curr = ranges[i]
            start, end = map(int, curr.split('-')) 
            erStart, eREnd = map(int, last.split('-'))
            # If current interval overlaps with the last merged
            # interval, merge them 
            if start <= eREnd:
                last = f"{erStart}-{max(eREnd, end)}"
                combinedOverlappingRanges[-1] = last
            else:
                combinedOverlappingRanges.append(curr)

        totalInclusiveIds = 0
        for r in combinedOverlappingRanges:
             start, end = map(int, r.split('-'))
             totalInclusiveIds += (end - start) + 1

        return totalInclusiveIds
def Day_6_pt_1():
    with open("Advent2025Resources/day_6_input.txt") as file:
        lines = file.readlines()
        signs = list(lines[-1].replace(" ","").replace("\n",""))
        cols = [0 if sign == '+' else 1 for sign in signs]
        for line in lines[:-1]:
            num = ''
            i = 0
            for char in list(line):
                if char == ' ' or char == '\n':
                    if len(num) > 0:
                        if signs[i] == '+':
                            cols[i] += int(num)
                        else:
                            cols[i] *= int(num)
                        num = ''
                        i += 1

                    continue
                else:
                    num += char
        return sum(cols)
    
def Day_6_pt_2():
    with open("Advent2025Resources/day_6_input.txt") as file:
        lines = file.readlines()
        signs = list(lines[-1].replace(" ","").replace("\n",""))
        cols = [[] for _ in range(len(signs))]
        for line in lines[:-1]:
            num = ''
            i = 0
            nextNumberIndex = 0
            signLine = list(lines)[-1]
            signLine += '\n' # add a newline to the end of the sign line to prevent index out of range error when checking for the next symbol after the last sign
            for posRef, char in enumerate(list(line)):
                for index, symbol in enumerate(list(signLine)[nextNumberIndex + 1:]):
                     if symbol != ' ':
                        if symbol == '\n':
                            nextNumberIndex = index + 1
                        else:
                            nextNumberIndex = nextNumberIndex + index
                        break
                if posRef == nextNumberIndex or char == '\n':
                    cols[i].append(num)
                    i += 1
                    if char == '\n':
                        break
                    num = ''
                    nextNumberIndex += 1 
                else:  
                    num += char

        total = 0
        for i in range(len(signs)):
            if signs[i] == '+':
                cephSum = 0
                maxLen = max(len(s) for s in cols[i])
                for char in range(maxLen)[::-1]:
                    constructedNum: str = ''
                    for num in list(cols[i]):
                        digit: str = num[char]
                        if digit != ' ':
                            constructedNum += digit   
                    cephSum += int(constructedNum)
                    print(f"+{constructedNum}")           
                total += cephSum
            else:
                cephProd = 1
                maxLen = max(len(s) for s in cols[i])
                for char in range(maxLen)[::-1]:
                    constructedNum: str = ''
                    for num in list(cols[i]):
                        digit: str = num[char]
                        if digit != ' ':
                            constructedNum += digit   
                    cephProd *= int(constructedNum)
                    print(f"x{constructedNum}")           
                total += cephProd
        return total
    
def Day_7_pt_1():
    def printLines(lines):
        for l in lines:
            print(l.strip('\n'))

    with open("Advent2025Resources/day_7_input.txt") as file:
        start = 'S'
        beam = '|'
        splitter = '^'
        lines = file.readlines()
        sIndex = lines[0].find(start)
        lines[1] = lines[1][:sIndex] + beam + lines[1][sIndex + 1:]
        splitCount = 0
        splitterCount = 0
        for lineNumber in range(2, len(lines)):
            for charIndex in range(len(lines[lineNumber].strip('\n'))):
                # Line has a splitter and there is a beam above it
                if lines[lineNumber][charIndex] == splitter and lines[lineNumber - 1][charIndex] == beam:
                    posToChange = [lines[lineNumber][charIndex-1] , lines[lineNumber][charIndex + 1]]
                    # print(f"Splitter {splitterCount}: {posToChange}")
                    splitterCount+= 1
                    splitCount = splitCount + sum(1 for p in posToChange if p != beam)
                    lines[lineNumber] = lines[lineNumber][:charIndex - 1] + beam + splitter + beam + lines[lineNumber][charIndex + 2:]

                # Line has a beam above it and is not a splitter
                if lines[lineNumber][charIndex] != splitter and lines[lineNumber - 1][charIndex] == beam:
                    lines[lineNumber] = lines[lineNumber][:charIndex] + beam + lines[lineNumber][charIndex + 1:]
        # printLines(lines) 
        return splitterCount
def Day_7_pt_2():
    def printLines(lines):
        for l in lines:
            print(l)
    with open("Advent2025Resources/day_7_input.txt") as file:
        start = 'S'
        splitter = '^'
        fLines = file.readlines()
        cellCollection = []
        for line in fLines:
            line = line.strip()  # Remove newline
            constructedCell = '|'.join(line)  # Add pipes between chars
            constructedCell += '\n'
            cellCollection.append(constructedCell)
        printLines(cellCollection)
        sIndex = cellCollection[0].find(start)
        cellCollection[1] = cellCollection[1][:sIndex] + '1' + cellCollection[1][sIndex + 1:]
        cellCollection = [constructedCell.strip().split('|') for constructedCell in cellCollection]
        print(cellCollection)
        print(len(cellCollection))
        print(len(cellCollection))
        for cellRow in range(2, len(cellCollection)):
            for cell in range(len(cellCollection[cellRow])):
                if cellCollection[cellRow][cell] != splitter and cellCollection[cellRow - 1][cell] != '.' and cellCollection[cellRow - 1][cell] != splitter:
                    computedChar = cellCollection[cellRow - 1][cell] if cellCollection[cellRow][cell] == '.' else (int(cellCollection[cellRow][cell]) + int(cellCollection[cellRow - 1][cell]))
                    cellCollection[cellRow] = cellCollection[cellRow][:cell] + [str(computedChar)] + cellCollection[cellRow][cell + 1:]
                if cellCollection[cellRow][cell] == splitter and cellCollection[cellRow - 1][cell] != '.':
                    print(cellCollection[cellRow][cell])
                    numberAboveSplitter = cellCollection[cellRow - 1][cell]
                    leftCharToReplace = cellCollection[cellRow][cell - 1]
                    rightCharToReplace = cellCollection[cellRow][cell + 1]
                    leftProp = numberAboveSplitter if leftCharToReplace == '.' else int(leftCharToReplace) + int(numberAboveSplitter) 
                    rightProp = numberAboveSplitter if rightCharToReplace == '.' else int(rightCharToReplace) + int(numberAboveSplitter)
                    cellCollection[cellRow] = cellCollection[cellRow][:cell - 1] + [str(leftProp)] + [splitter] + [str(rightProp)] + cellCollection[cellRow][cell + 2:]
                # .|.|.|.|.|.|.|S|.|.|.|.|.|.|.
                # .|.|.|.|.|.|.|.|.|.|.|.|.|.|.
                # .|.|.|.|.|.|1|^|1|.|.|.|.|.|.
                # .|.|.|.|.|.|1|.|1|.|.|.|.|.|.
                # .|.|.|.|.|1|^|2|^|1|.|.|.|.|.
                # .|.|.|.|.|1|.|2|.|1|.|.|.|.|.
                # .|.|.|.|1|^|3|^|3|^|1|.|.|.|.
                # .|.|.|.|1|.|3|.|3|.|.|.|.|.|.
                # .|.|.|1|^|4|^|3|3|1|^|1|.|.|.
                # .|.|.|1|.|4|.|.|.|1|.|1|.|.|.
                # .|.|1|^|5|^|4|3|4|^|2|^|1|.|.
                # .|.|1|.|5|.|4|3|4|.|2|.|1|.|.
                # .|1|^|1|5|4|^|7|4|.|2|1|^|1|.
                # .|1|.|1|5|4|.|7|4|.|2|1|.|1|.
                # 1|^|2|^|T|^|E|^|E|^|2|1|1|^|1
                # 1|.|2|.|T|.|E|.|E|.|2|1|1|.|1
                #Populates down and combines 
        printLines(cellCollection)
        return sum(int(cell) for cell in cellCollection[-1] if cell != '.')
def Day_7_pt_2_dep():
    def printLines(lines):
        for l in lines:
            print(l.strip('\n'))
    with open("Advent2025Resources/day_7_input_test.txt") as file:
        start = 'S'
        splitter = '^'
        lines = file.readlines()
        sIndex = lines[0].find(start)
        lines[1] = lines[1][:sIndex] + '1' + lines[1][sIndex + 1:]
        for lineNumber in range(2, len(lines)):
            for charIndex in range(len(lines[lineNumber].strip('\n'))):
                if lines[lineNumber][charIndex] != splitter and lines[lineNumber - 1][charIndex] != '.' and lines[lineNumber - 1][charIndex] != splitter:
                    computedChar = lines[lineNumber - 1][charIndex] if lines[lineNumber][charIndex] == '.' else (int(lines[lineNumber][charIndex]) + int(lines[lineNumber - 1][charIndex]))
                    lines[lineNumber] = lines[lineNumber][:charIndex] + str(computedChar) + lines[lineNumber][charIndex + 1:]
                if lines[lineNumber][charIndex] == splitter and lines[lineNumber - 1][charIndex] != '.':
                    print(lines[lineNumber][charIndex])
                    numberAboveSplitter = lines[lineNumber - 1][charIndex]
                    leftCharToReplace = lines[lineNumber][charIndex - 1]
                    rightCharToReplace = lines[lineNumber][charIndex + 1]
                    leftProp = numberAboveSplitter if leftCharToReplace == '.' else int(leftCharToReplace) + int(numberAboveSplitter) 
                    rightProp = numberAboveSplitter if rightCharToReplace == '.' else int(rightCharToReplace) + int(numberAboveSplitter)
                    lines[lineNumber] = lines[lineNumber][:charIndex - 1] + str(leftProp) + splitter + str(rightProp) + lines[lineNumber][charIndex + 2:]

                # Line has a beam above it and is not a splitter
                
        printLines(lines)


def Day_8_pt_1():
    def tablePrint(coordinatePairs):
        print(f"{'INDEX':<6} | {'ORIGIN (c1)':<20} | {'NEAREST (c2)':<20} | {'DISTANCE'}")
        print("—" * 75)
        for idx, entry in enumerate(coordinatePairs):
            c1 = f"({entry['c1']['x']},{entry['c1']['y']},{entry['c1']['z']})"
            c2 = f"({entry['c2']['x']},{entry['c2']['y']},{entry['c2']['z']})"
            dist = entry['distance']
            
            # Color-coding the distance for visibility (optional, works in most terminals)
            # If the distance is float('inf'), we print 'None'
            dist_str = f"{dist:,.2f}" if dist != float('inf') else "N/A"
            
            print(f"{idx:<6} | {c1:<20} | {c2:<20} | {dist_str}")

        print("—" * 75)
    #d(p, q) = √[(p₁ - q₁)² + (p₂ - q₂)² + (p₃ - q₃)²]
    pythagoras3D = lambda point1, point2:  (((point1['x'] - point2['x']) ** 2) + ((point1['y'] - point2['y']) ** 2) + ((point1['z'] - point2['z']) ** 2)) ** 0.5  # noqa: E731
    with open("Advent2025Resources/day_8_input_test.txt") as file:
        lines = file.readlines()
        coordinates = []
        for line in lines:
            coords = [c.strip('\n') for c in line.split(',')]
            coordinates.append({'x': int(coords[0]), 'y' : int(coords[1]), 'z': int(coords[2])})
        coordinatePairs = []
        for i in range(len(coordinates)):
            coordinatePair = {
                'c1': coordinates[i], 
                'distance': float('inf'),
                'c2': None
                }
            for ii in range(1 ,len(coordinates)):
                distance = pythagoras3D(coordinates[i], coordinates[ii])
                if distance > 0 and distance < coordinatePair['distance']:
                    coordinatePair['c2'] = coordinates[ii]
                    coordinatePair['distance'] = distance
            coordinatePairs.append(coordinatePair)
        coordinatePairs.sort(key=lambda c: c['distance'])
        circuits = [[coordinatePairs[0]['c1'], coordinatePairs[0]['c2']]]
        for pairIndex in range(1, len(coordinatePairs)):
            for circuitIndex, circuit in enumerate(circuits):
                initialCircuitLength = len(circuit)
                cordPair1 = coordinatePairs[pairIndex]['c1']
                cordPair2 = coordinatePairs[pairIndex]['c2']
                if cordPair1 in circuit and cordPair2 in circuit:
                    break
                for coordinate in circuit:
                    if cordPair1 == coordinate:
                        circuits[circuitIndex].append(cordPair2)
                        break
                    if cordPair2 == coordinate:
                        circuits[circuitIndex].append(cordPair1)
                        break
                if initialCircuitLength == len(circuit):
                    circuits.append([coordinatePairs[pairIndex]['c1'], coordinatePairs[pairIndex]['c2']])
        print(circuits)
        tablePrint(coordinatePairs)
        
               
if __name__ == "__main__":
    # print(Day_1())
    # print(Day_1_pt_2()) # dear god
    # print(Day_2_pt_1())
    # print(Day_2_pt_2())
    # print(Day_3_pt_1())
    # print(Day_3_pt_2_v2())
    # print(Day_4_pt_2())
    # print(Day_5_pt_1())
    # print(Day_5_pt_2())
    # print(Day_6_pt_2()) # Holy absolute fuck
    # print(Day_7_pt_2()) # There is no way i got this first try,
    print(Day_8_pt_1())
    pass















def Day_3_pt_1():
    with open("Advent2025Resources/day_3_input.txt") as file:
        maximumJoltage = 0
        for bank in file:
            bank = list(set(bank.strip()))
            for baseIndex in range(len(bank)):
                for compareIndex in range(0, len(bank) -1):
                    if bank[compareIndex] < bank[compareIndex + 1]:
                        temp = bank[compareIndex]
                        bank[compareIndex] = bank[compareIndex + 1]
                        bank[compareIndex + 1] = temp
            maximumJoltage += int(f"{bank[0]}{bank[1]}")
    return maximumJoltage