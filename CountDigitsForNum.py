#while loop - count digits for a number until the sum is less than 10

def countDigits(num: int):
    cntTimes = 0
    digList: int = []
    while num >= 10:
        cntTimes += 1
        digList.clear()
        numStr = str (num)
        for i in range(len(numStr)):
            digList.append(int(numStr[i]))
        num = 0
        for item in digList:
            num += item

    return 
#nameList: str = ["Dixen", "Yuxi", "Ling"]

while 1:
    str1 = input("Input a integer number or Q/q to exit: ")
    if str1 == 'Q' or str1 == 'q':
        break
    else:
        num1 = int(str1)
        print(f"Result is {countDigits(num1)}")
