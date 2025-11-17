#Recursive Function - count digits for a number until the sum is less than 10

def countDigits(num: int, cntTimes: int = 0):
    digList: int = []
    if num >= 10:
        cntTimes += 1
        digList.clear()
        numStr = str (num)

        for i in range(len(numStr)):
            digList.append(int(numStr[i]))
        num = 0

        for item in digList:
            num += item

        cntTimes = countDigits(num, cntTimes)   #recursion

    return cntTimes

num = int(input("Input a integer number - by recursion: "))
print(f"Result is {countDigits(num)}")
