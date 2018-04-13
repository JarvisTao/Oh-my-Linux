import calculator
from functools import reduce
print('25 + 56 = {}'.format(calculator.add(25, 56)))
print('86 - 68 = {}'.format(calculator.sub(86, 68)))
print('50 * 60 = {}'.format(calculator.multi(50, 60)))
print('99 / 25 = {}'.format(calculator.div(99, 25)))
print()
#**********************************************
def canBeDived(x):
    if x % 3 == 0 and x % 5 == 0:
        return True
print(list(filter(canBeDived,range(0,100))))
print()

#**********************************************
def sumODD(x, y):
    if y % 2 != 0:
        return x + y
    return x

print(reduce(sumODD,range(1,100)))
print()

#**********************************************
def power3(x):
    return x ** 3

print(list(map(power3, range(0,101,2))))
print()
#**********************************************
def gcdIter(a, b):
    maxNum = a if a > b else b
    minNum = b if a > b else a 
    while (maxNum % minNum) != 0:
        if (maxNum % minNum) > minNum:
            maxNum = maxNum % minNum
        else:
            tempNum = maxNum % minNum
            maxNum = minNum
            minNum = tempNum
    return minNum

def gcdRecur(a, b):
    maxNum = a if a > b else b
    minNum = b if a > b else a 
    if maxNum % minNum == 0:
        return minNum
    else:
        return gcdRecur(maxNum % minNum, minNum)
print(gcdIter(12,9))
print(gcdRecur(12,9))
        




