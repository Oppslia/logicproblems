from enum import Enum
def isSq(n):
   return (n ** 0.5) % 1
def sq(n):
    return n ** 0.5
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 5 and n % 5 == 0:
        return False
    for i in range(2, sq(n) + 1):
        if(n % i) == 0:
            return False
    else:
        return True
## Problem 0:
def Problem_0():
    oddSquareSum = 0
    CurrentIterator = 0
    allSquares = 0
    while allSquares < 566000:
        allSquares = allSquares + 1

        if CurrentIterator % 2 != 0:
            oddSquareSum = oddSquareSum + (CurrentIterator * CurrentIterator)
        CurrentIterator = CurrentIterator + 1

    return oddSquareSum
## Problem 1: Multiples of 3 or 5
def Problem_1():
    multipleSum = 0
    for n in range(0, 1000):
        if (n % 3 == 0) or (n % 5 == 0):
            multipleSum = multipleSum + n
    return multipleSum
## Problem 2: Even Fibonacci Numbers
def Problem_2(fib: int):
    sumOfAllEvenFibs = 0
    a = 0
    b = 1
    c = None
    while a < fib:
        c = b
        b = a
        a = b + c
        if a % 2 == 0:
            sumOfAllEvenFibs = sumOfAllEvenFibs + a
    return sumOfAllEvenFibs
## Problem 3: Largest Prime Factor
def Problem_3(n: int):
    x = 2 # First factor
    while x * x <= n:  # Doesn't go over halfway point, because you can't divide something evenly past the half way point.
        while (n / x) % 1 == 0 and x < n: # While n(Divisor) is divisble by x and x is less then the dividend. Loop until you cant divide it by the divisor anymore.
            n //= x # set the Dividend = to the newly reduced number.
        x = x + 1 
    return n

## Problem 4: Largest Palindrome from the product of two 3 digit numbers
def Problem_4():
    def isPalinDrome(x:int):
        num = x
        rev = 0
        while (num > 0):
            dig = num % 10
            rev = rev * 10 + dig
            num //= 10
        return rev == x
    num = 999
    largestPalindrome = 0
    while num > 0:
        if largestPalindrome != 0 and num * num < largestPalindrome:
            return largestPalindrome
        multiplier = num
        while multiplier > 0:
            product = multiplier * num
            if product <= largestPalindrome:
                break
            if isPalinDrome(product):
                largestPalindrome = product
            else:
                multiplier = multiplier - 1
        num = num - 1
        
    return largestPalindrome


# Problem 5: Smallest Multiple of numbers [1-20]:
def Problem_5():
    mn = 1
    mx = 20
    smallestMultiple = 1
    primes = [x for x in range(mn, mx + 1) if isPrime(x)]
    for x in primes:
        highestPowerLessThanMax = 0
        for p in range(mn, mx, 1):
           if x ** p <= mx:
               highestPowerLessThanMax = p
        smallestMultiple = smallestMultiple * (x ** highestPowerLessThanMax)
    return smallestMultiple
            

def Problem_6(n):
    sumOfSquares = sum([x ** 2 for x in range(1, n+ 1)])
    squareOfSum = sum([x for x in range(1, n+ 1)]) ** 2
    return squareOfSum - sumOfSquares

#Provlem 7: What is the 10001st prime number?
def Problem_7(n):
    primeCount = 0
    subject = 0
    while primeCount != n:
        if isPrime(subject):
            primeCount = primeCount + 1
        if primeCount == n:
            return subject
        else: 
            subject = subject + 1
    return subject

def Problem_8(n: str, adjacentCount: int):
    highest= 0
    for x in range(len(n)):
        adjacent = ([int(acc) for acc in n[x:x+adjacentCount]])
        adjacentProduct = 1
        for acc in adjacent:
            adjacentProduct *= acc
        if highest < adjacentProduct:
            highest = adjacentProduct
    return highest

def Problem_9(n):
    for a in range(1 , n + 1):
        for b in range(1 , n + 1):
            c = n - a - b
            if a ** 2 +  b ** 2 == c ** 2:
                return a * b * c

def Problem_10(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

def Problem_11(colWidth):
    grid = [8,2,22,97,38,15,00,40,00,75,4,5,7,78,52,12,50,77,91,8,
            49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,00,
            81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65,
            52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91,
            22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,
            24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50,
            32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,
            67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21,
            24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,
            21,36,23,9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95,
            78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92,
            16,39,5,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57,
            86,56,00,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58,
            19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40,
            4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66,
            88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69,
            4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36,
            20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16,
            20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54,
            1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]
    def DiagonalCheck(index):
        def br(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position + colWidth + 1
                position = newPos
                total *=  grid[newPos]
            return total
        def bl(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position + colWidth - 1
                position = newPos
                total *=  grid[newPos]
            return total
        def ur(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position - colWidth + 1
                position = newPos
                total *=  grid[newPos]
            return total
        def ul(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position - colWidth - 1
                position = newPos
                total *=  grid[newPos]
            return total
        values = []
        try:
            values.append(br(index))
        except:
            pass

        try:
            values.append(bl(index))
        except:
            pass

        try:
            values.append(ur(index))
        except:
            pass

        try:
            values.append(ul(index))
        except:
            pass

        if values:
            return max(values)
    def HorizontalCheck(index):
        def right(i):
            total = grid[i]
            for x in range(3):
                total *= grid[i + x]
            return total
        def left(i):
            total = grid[i]
            for x in range(3):
                total *= grid[i - x]
            return total
        values = []
        try:
            values.append(left(index))
        except:
            pass
        try:
            values.append(right(index))
        except:
            pass
        if values:
            return max(values)
    def VeticalCheck(index):
        def up(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position - colWidth
                position = newPos
                total *=  grid[newPos]
            return total
        def down(i):
            total = grid[i]
            position = i
            for x in range(3):
                newPos = position + colWidth
                position = newPos
                total *=  grid[newPos]
            return total
        values = []
        try:
            values.append(up(index))
        except:
            pass
        try:
            values.append(down(index))
        except:
            pass
        if values:
            return max(values)
    highestProduct = 0
    for x in range(len(grid)):
        maxDiag = DiagonalCheck(x) or 0
        maxHori = HorizontalCheck(x) or 0
        maxVert = VeticalCheck(x) or 0
        if(max(maxDiag, maxHori, maxVert) > highestProduct):
            highestProduct = max(maxDiag, maxHori, maxVert)
    
    return highestProduct

def Problem_12(divisorCount):
    def getDivisorCount(n):
        count = 0
        # We use int(n**0.5) + 1 to make sure the loop includes the square root
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:  # If n is divisible by x
                
                # CASE A: x is exactly the square root (e.g., 6 * 6 = 36)
                if x * x == n:
                    count += 1 
                    
                # CASE B: x is a normal factor (e.g., 2 into 36 gives 18)
                else:
                    count += 2 # We count both x AND n/x
        return count
    triangle = 0
    inc = 1
    while True:
        triangle += inc
        if getDivisorCount(triangle) > divisorCount:
            return triangle
        else:
            inc += 1
        

def Problem_13():
    nums = [37107287533902102798797998220837590246510135740250,46376937677490009712648124896970078050417018260538,74324986199524741059474233309513058123726617309629,91942213363574161572522430563301811072406154908250,23067588207539346171171980310421047513778063246676,89261670696623633820136378418383684178734361726757,28112879812849979408065481931592621691275889832738,44274228917432520321923589422876796487670272189318,47451445736001306439091167216856844588711603153276,70386486105843025439939619828917593665686757934951,62176457141856560629502157223196586755079324193331,64906352462741904929101432445813822663347944758178,92575867718337217661963751590579239728245598838407,58203565325359399008402633568948830189458628227828,80181199384826282014278194139940567587151170094390,35398664372827112653829987240784473053190104293586,86515506006295864861532075273371959191420517255829,71693888707715466499115593487603532921714970056938,54370070576826684624621495650076471787294438377604,53282654108756828443191190634694037855217779295145,36123272525000296071075082563815656710885258350721,45876576172410976447339110607218265236877223636045,17423706905851860660448207621209813287860733969412,81142660418086830619328460811191061556940512689692,51934325451728388641918047049293215058642563049483,62467221648435076201727918039944693004732956340691,15732444386908125794514089057706229429197107928209,55037687525678773091862540744969844508330393682126,18336384825330154686196124348767681297534375946515,80386287592878490201521685554828717201219257766954,78182833757993103614740356856449095527097864797581,16726320100436897842553539920931837441497806860984,48403098129077791799088218795327364475675590848030,87086987551392711854517078544161852424320693150332,59959406895756536782107074926966537676326235447210,69793950679652694742597709739166693763042633987085,41052684708299085211399427365734116182760315001271,65378607361501080857009149939512557028198746004375,35829035317434717326932123578154982629742552737307,94953759765105305946966067683156574377167401875275,88902802571733229619176668713819931811048770190271,25267680276078003013678680992525463401061632866526,36270218540497705585629946580636237993140746255962,24074486908231174977792365466257246923322810917141,91430288197103288597806669760892938638285025333403,34413065578016127815921815005561868836468420090470,23053081172816430487623791969842487255036638784583,11487696932154902810424020138335124462181441773470,63783299490636259666498587618221225225512486764533,67720186971698544312419572409913959008952310058822,95548255300263520781532296796249481641953868218774,76085327132285723110424803456124867697064507995236,37774242535411291684276865538926205024910326572967,23701913275725675285653248258265463092207058596522,29798860272258331913126375147341994889534765745501,18495701454879288984856827726077713721403798879715,38298203783031473527721580348144513491373226651381,34829543829199918180278916522431027392251122869539,40957953066405232632538044100059654939159879593635,29746152185502371307642255121183693803580388584903,41698116222072977186158236678424689157993532961922,62467957194401269043877107275048102390895523597457,23189706772547915061505504953922979530901129967519,86188088225875314529584099251203829009407770775672,11306739708304724483816533873502340845647058077308,82959174767140363198008187129011875491310547126581,97623331044818386269515456334926366572897563400500,42846280183517070527831839425882145521227251250327,55121603546981200581762165212827652751691296897789,32238195734329339946437501907836945765883352399886,75506164965184775180738168837861091527357929701337,62177842752192623401942399639168044983993173312731,32924185707147349566916674687634660915035914677504,99518671430235219628894890102423325116913619626622,73267460800591547471830798392868535206946944540724,76841822524674417161514036427982273348055556214818,97142617910342598647204516893989422179826088076852,87783646182799346313767754307809363333018982642090,10848802521674670883215120185883543223812876952786,71329612474782464538636993009049310363619763878039,62184073572399794223406235393808339651327408011116,66627891981488087797941876876144230030984490851411,60661826293682836764744779239180335110989069790714,85786944089552990653640447425576083659976645795096,66024396409905389607120198219976047599490197230297,64913982680032973156037120041377903785566085089252,16730939319872750275468906903707539413042652315011,94809377245048795150954100921645863754710598436791,78639167021187492431995700641917969777599028300699,15368713711936614952811305876380278410754449733078,40789923115535562561142322423255033685442488917353,44889911501440648020369068063960672322193204149535,41503128880339536053299340368006977710650566631954,81234880673210146739058568557934581403627822703280,82616570773948327592232845941706525094512325230608,22918802058777319719839450180888072429661980811197,77158542502016545090413245809786882778948721859617,72107838435069186155435662884062257473692284509516,20849603980134001723930671666823555245252804609722,53503534226472524250874054075591789781264330331690]
    return str(sum(nums))[0:10]
# Longest Collatz Sequence under 1,000,000
def Problem_14(n):
    formula = lambda a: a // 2 if a % 2 == 0 else 3 * a + 1  # noqa: E731
    chainCount = 0
    longestChainCount = chainCount
    startingNumberWithLongestChain = 0
    for startingNumber in range(0, n):
        chainNumber = startingNumber
        while True:
            if chainCount > longestChainCount:
                longestChainCount = chainCount
                startingNumberWithLongestChain = startingNumber
            if chainNumber <= 1 :
                chainCount = 0
                break
            chainNumber = formula(chainNumber)
            chainCount += 1
    return startingNumberWithLongestChain


def Problem_15(gridSize):
    # n! / K!(n-k)!
    # grid of 3 x 3 = 6 total moves. n = 6. each direction can only have 3. k = 3:
    #  6*5*4*3*2*1 / (3*2*1)* (6-3) *2*1
    def f(sub): 
        numerator = sub
        for multiplier in range(1, sub):
            numerator = numerator * (sub - multiplier)
        return numerator
    numerator = f(gridSize * 2) # Total Moves
    denominator = f(gridSize) # Total Moves in a single direction
    return int(numerator / (denominator * denominator))
    
        
def Problem_16(power):
    return sum(int(i) for i in str(2**power))

def Problem_17():
    class LessThan20(Enum):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9
        ten = 10
        eleven = 11
        twelve = 12
        thirteen = 13
        fourteen = 14
        fifteen = 15
        sixteen = 16
        seventeen = 17
        eighteen = 18
        nineteen = 19
    class Intervals(Enum):
        twenty = 20
        thirty = 30
        forty = 40
        fifty = 50
        sixty = 60
        seventy = 70
        eighty = 80
        ninety = 90
        hundred = 100
        thousand = 1000
    totalWordCount = 0
    for x in range(1,1001):
        if x < 20:
            totalWordCount += len(LessThan20(x).name)
        if x >= 20 and x < 100:
            if str(x)[1] == '0':
                totalWordCount += len(Intervals(x).name)
            else:
                totalWordCount += len(Intervals(int(f"{str(x)[0]}0")).name + LessThan20(int(str(x)[1])).name)
        if x >= 100 and x < 1000: # hundreds
            if x % 100 == 0:
                totalWordCount += len(f"{LessThan20(int(str(x)[0])).name}{Intervals(100).name}")
                continue
            else:
                word = f"{LessThan20(int(str(x)[0])).name}{Intervals(100).name}and"
                if int(str(x)[1:]) < 20:
                    word += LessThan20(int(str(x)[1:])).name
                if int(str(x)[1:]) >= 20:
                    if str(x)[2] == '0':
                        word += Intervals(int(str(x)[1:])).name
                    else:
                        word += Intervals(int(f"{str(x)[1]}0")).name + LessThan20(int(str(x)[2])).name
                totalWordCount += len(word)
        if x == 1000:
            totalWordCount += len(f"{LessThan20(int(str(x)[0])).name}{Intervals(1000).name}")
    return totalWordCount
        
def Problem_18():
    pyramidNums = [75,
        95,64,
        17,47,82,
        18,35,87,10,
        20,4,82,47,65,
        19,1,23,75,3,34,
        88,2,77,73,7,63,67,
        99,65,4,28,6,16,70,92,
        41,41,26,56,83,40,80,70,33,
        41,48,72,33,47,32,37,16,94,29,
        53,71,44,65,25,43,91,52,97,51,14,
        70,11,33,28,77,73,17,78,39,68,17,57,
        91,71,52,38,17,14,91,43,58,50,27,29,48,
        63,66,4,68,89,53,67,30,73,16,69,87,40,31,
        4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
 
    currentHighestRowIndex = 0
    total = pyramidNums[currentHighestRowIndex]
    row = 1
    while True:
            try:
                adjacentNums = pyramidNums[currentHighestRowIndex + row: currentHighestRowIndex + row + 2] # slice is weird and needs 2 ro return 2 items 
                total += max(adjacentNums)
                print(max(adjacentNums))
                currentHighestRowIndex += row if adjacentNums[0] > adjacentNums[1] else row + 1
                row += 1
            except:
                return total
def Problem_18_2():
    pyramid = [
                      [75],
                     [95, 64],
                    [17, 47, 82],
                   [18, 35, 87, 10],
                  [20, 4, 82, 47, 65],
                 [19, 1, 23, 75, 3, 34],
                [88, 2, 77, 73, 7, 63, 67],
               [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
          [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
         [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]
    for row in range(len(pyramid) - 2, -1, -1):
        for col in range(len(pyramid[row])):
            left_child = pyramid[row + 1][col]
            right_child = pyramid[row + 1][col + 1]
            pyramid[row][col] += max(left_child, right_child)

    return pyramid[0][0]

def Problem_19():
    class Day(Enum):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6
    class DayCount(Enum):
        JANUARY = 31
        FEBRUARY = 28
        MARCH = 31
        APRIL = 30
        MAY = 31
        JUNE = 30
        JULY = 31
        AUGUST = 31
        SEPTEMBER = 30
        OCTOBER = 31
        NOVEMBER = 30
        DECEMBER = 31
    class Month():
        def __init__(self, leapYear: bool, month: DayCount):
            self.name = month.name
            self.days = month.value if month.name != DayCount.FEBRUARY.name and not leapYear else 29
    class Year():
        leapYear = False
        days = 365
        name = ''
        firstDayStartsOn = Day.SUNDAY
        def __init__(self, year):
            self.name = str(year)
            self.leapYear = True if year % 4 == 0 and year % 400 != 0 else False
            if self.leapYear:
                self.days = 366
    firstOfMonthSundays = 0   
    currentDay = Day.SUNDAY
    currentYear = 1901
    def cycleDays(days: int):
        print(currentYear)
        nonlocal firstOfMonthSundays, currentDay
        if currentDay == Day.SUNDAY:
            firstOfMonthSundays = firstOfMonthSundays  + 1

        currentDayIndex = (currentDay.value + days) % 7        
        currentDay = list(Day)[currentDayIndex]
    while True:
        year = Year(currentYear)
        for monthName in list(DayCount.__members__.keys()):
            cycleDays(Month(year.leapYear, DayCount[monthName]).days)
            if year.name == '2000':
                return firstOfMonthSundays
        currentYear += 1

#Factorial Digit Sum
def Problem_20(digit):
    total = digit
    for multiplierReduction in range(digit):
        total = total * (digit - multiplierReduction)
    
    digitSum = 0
    for num in str(total):
        digitSum += int(num)
    return digitSum

def Problem_21(n):
    def getDivisors(num):
        divs = {1} # 1 is always a proper divisor
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divs.add(i)
                divs.add(num // i)
        return divs
    amicable = []
    for a in range(n):
        b = sum(getDivisors(a))
        if a != b and sum(getDivisors(b)) == a:
            amicable.append(a)        
    return sum(amicable)
def Problem_22(): 
    score = 0
    with open("C:\\Users\\ShawnSeltner\\names.txt") as file:
        lines = file.read().split(',')
        lines.sort()
        for index, line in enumerate(lines):
            lineScore = 0
            for char in line.strip('"'):
                lineScore += (ord(char.upper()) % 64) ## offset from 65 by 1 to give A a value of 1 and not O
            score += lineScore * (index + 1)
            lineScore = 0
    return score        

def Problem_23():
    def markDivisors(num):
        divs = {1} # 1 is always a proper divisor
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divs.add(i)
                divs.add(num // i)
        if sum(divs) > num:
            return True
        else:
            return False
    numbers = [True] * 28123
    abundantNumbers = []
    for n in range(12, 28123):
        if markDivisors(n):
            abundantNumbers.append(n)
    for x in abundantNumbers:
        for y in abundantNumbers:
            if x + y < 28123:
                numbers[x + y] = False
    return sum(x for x, i in enumerate(numbers) if i)

# def Problem_24(nums):
#     permutations = []
#     state = [{index : num} for index, num in enumerate(range(len(nums)))]
#     i = 0
#     while True:
#         permutation = ''
#         for x in range(0, len(nums)):
#             state[x] = 
#             permutation += str(nums[i + x])
#         permutations.append(permutation)
#         i += 1

def Problem_25():
    a = 0
    b = 1
    c = None
    count = 0
    while True:
        c = b
        b = a
        a = b + c
        count += 1
        if (len(str(a)) == 1000):
            return count

def Problem_26(limit):
    longest = 0
    result = 0
    #Track the remainder. Once a remainder appears again, the pattern has completed a cycle. Here is the forumla
    # a = b x q(0) + r | q = 0 in this case
    # remainder of ((r * 10) / b ) = q becomes r for next iteration same equation but * 10 for decimal numbers
    # Example = a = 1 b = 7
    #   a ÷ b = q        || 1 / 7 = 0.____ q = 0. remainder(r) = 1 ?? Still don't know why 1 evertime but it works
    #  (r * 10) / b = q  || (1 * 10) / 7 : q = 1, remainder(r) = 3
    #                       (3 * 10) / 7 : q = 4, remainder(r) = 2
    #                       (2 * 10) / 7 : q = 2, remainder(r) = 6
    #                       (6 * 10) / 7 : q = 8, remainder(r) = 4
    #                       (4 * 10) / 7 : q = 5, remainder(r) = 5
    #                       (5 * 10) / 7 : q = 7, remainder(r) = 1 --- repeat
    #                       (1 * 10) / 7 : q = 1, remainder(r) = 3
    #                       ect....

    for b in range(2, limit):
        a = 1
        seen = {}
        remainder = a % b
        position = 0

        while remainder != 0 and remainder not in seen: # When the remainder repeats this turns false
            seen[remainder] = position
            remainder = (remainder * 10) % b
            position += 1

        if remainder != 0:
            cycle_length = position - seen[remainder] # then we get the current position(end or 6) and subtract the first time the remainder occured(0 position) so 6 is the length
            if cycle_length > longest:
                longest = cycle_length
                result = b

    return result

def Problem_28(gridSize):
    gridMaxNum = gridSize * gridSize
    currentInterval = 2
    diagonalTotal = 1
    currentDiagonal = 1
    while currentDiagonal != gridMaxNum:
        for i in range(4):
            currentDiagonal += currentInterval
            diagonalTotal += currentDiagonal
        currentInterval += 2    
    return diagonalTotal
   # 669171001

def Problem_30(power):
    maxPossibleNumber = power * (9**power)
    numbers= [] 
    for x in range(2, maxPossibleNumber):
        number = x
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        digits.reverse() 
        total = 0
        for d in digits:
            total += d ** power
        if x == total:
            numbers.append(x)
    return sum(numbers)

def Problem_33():
    def simple_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    productNumerator = 1
    productDenominator = 1
    for numerator in range(10,100):
        for denominator in range(numerator, 100):
            if numerator == denominator:
                continue
            common_digit = None
            for digit in str(numerator):
                if digit in str(denominator):
                    common_digit = digit
                    break # We found a match, so we stop looking
            if not common_digit:
                continue
            if '0' in common_digit:
                continue
            if common_digit:
                newNumerator= str(numerator).replace(common_digit, '', 1) if str(numerator).replace(common_digit, '', 1) != '0' else None
                newDenominator = str(denominator).replace(common_digit, '', 1) if str(denominator).replace(common_digit, '', 1) != '0' else None
                if newNumerator is None or newDenominator is None:
                    continue
                if int(newNumerator) / int(newDenominator) == numerator / denominator:
                    productNumerator *= int(newNumerator)
                    productDenominator *= int(newDenominator)
    div = simple_gcd(productNumerator, productDenominator)
    print(div)
    return f"{productNumerator // div}/{productDenominator // div}"
            
def Problem_35():
    def arrayToNum(nums:list):
        number:int = 0
        length = len(nums)
        for index,num in enumerate(nums):
            place: int = length - index - 1
            number += num * (10 ** place)
        return number


    def getRotations(num):
        number = num
        rotations = []
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        digits.reverse()
        for i in range(len(digits)):
            rotatedNumber = digits[i:]
            rotatedNumber.extend(digits[:i])
            
            rotations.append(arrayToNum(rotatedNumber))
        
        return rotations

    circularPrimes = set()
    def filterNums(n):
        while n > 0:
            digit = n % 10
            if n > 10 and digit in [0,2,4,5,6,8]:
                return False
            n //= 10
        return True
    filteredNums = [num for num in range(1, 1000000) if filterNums(num)]
    for num in filteredNums:
        if num in circularPrimes or not isPrime(num):
            continue
        cyclePrimes = []
        rotations = getRotations(num)
        for rotation in rotations:
            if not isPrime(rotation):
                break
            else:
                cyclePrimes.append(rotation)
        if len(rotations) == len(cyclePrimes):
            circularPrimes.update(cyclePrimes)
    return len(circularPrimes),circularPrimes

def Problem_39():
    solution = {
        "p": 0,
        "solutions": 0
        }
    for p in range(1000):
        solCount = 0
        for a in range (p):
            for b in range(a):
                c = sq(a**2 + b**2)
                if c % 1 != 0:
                    continue
                if p == a + b + c:
                    solCount += 1
        if solution["solutions"] < solCount:
            solution["solutions"] = solCount
            solution["p"] = p

    return solution

def Problem_40():
    digit = 1
    total = 1
    while digit <= 1000:
        total += digit**digit
        digit += 1
    return str(total)[-10:]





if __name__ == "__main__":
        # print(Problem_0())
    # print(Problem_1())
    # print(Problem_2(4000000))
    # print(Problem_3(600851475143))
    # print(Problem_4())
    # print(Problem_5())
    # print(Problem_6(100))
    # #print(Problem_7(10001))
    # print(Problem_8(
    #     '73167176531330624919225119674426574742355349194934' \
    #     '96983520312774506326239578318016984801869478851843' \
    #     '85861560789112949495459501737958331952853208805511' \
    #     '12540698747158523863050715693290963295227443043557' \
    #     '66896648950445244523161731856403098711121722383113' \
    #     '62229893423380308135336276614282806444486645238749' \
    #     '30358907296290491560440772390713810515859307960866' \
    #     '70172427121883998797908792274921901699720888093776' \
    #     '65727333001053367881220235421809751254540594752243' \
    #     '52584907711670556013604839586446706324415722155397' \
    #     '53697817977846174064955149290862569321978468622482' \
    #     '83972241375657056057490261407972968652414535100474' \
    #     '82166370484403199890008895243450658541227588666881' \
    #     '16427171479924442928230863465674813919123162824586' \
    #     '17866458359124566529476545682848912883142607690042' \
    #     '24219022671055626321111109370544217506941658960408' \
    #     '07198403850962455444362981230987879927244284909188' \
    #     '84580156166097919133875499200524063689912560717606' \
    #     '05886116467109405077541002256983155200055935729725' \
    #     '71636269561882670428252483600823257530420752963450', 13))
    # print(Problem_9(1000))
    # print(Problem_10(2000000))
    # print(Problem_11(20)) # No way I solved this bro
    # # print(Problem_12(500))
    # print(Problem_13())
    # # print(Problem_14(1000000)) # No way I solved this either bro.
    # print(Problem_15(20))
    # print(Problem_16(1000))
    # print(Problem_18_2())
    # print(Problem_19())
    #print(Problem_20(100))
    #print(Problem_21(10000))
    #print(Problem_22())
    #print(Problem_23())
    # print(Problem_24())
    # print(Problem_26(1000))
    # print(Problem_28(1001)) # cant believe I solved this totally solo
    # print(Problem_30(5))
    #print(Problem_33())
    #print(Problem_35())
    #print(Problem_37())
    #print(Problem_39())
    print(Problem_40())