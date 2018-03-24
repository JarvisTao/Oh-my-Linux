#***********homework04-1*********************
print()
End = int(input("Please input the value of 'End':"))
i = 1
s = 0
while i <= End:
    s += i
    i = i + 1
print("The sum from 1 to %d is: %d" %(End, s))
print()

##***********homework04-2*********************
#print()
#cnt = 3
#while cnt:
#    num = int(input("Please input an integer: "))
#    if num % 2 == 0 and num % 3 == 0:
#        print("The %d can be divided by 2 and 3." %num)
#    elif num % 2 == 0:
#        print("The %d can be divided by 2." %num)
#    elif num % 3 == 0:
#        print("The %d can be divided by 3." %num)
#    else:
#        print("The %d can not be divided by 2 or 3." %num)
#    cnt = cnt - 1
#    print()
#        
#***********homework04-3*********************
for i in range(1, 1000):
    s = 0 
    factor =[]
    for j in range(1, i):
        if i % j == 0:
            s += j
            factor.append(j)
    if s == i:
        print (i, "its factors are ",end = "")
        for m in factor:
            print(m, end = ", ")
        print ("\b\b  ")
print()
    
#***********homework04-3*********************
print("The Narcissisic numbers in 1000 are:")
for i in range(100, 1000):
    if i == pow(i//100,3) + pow(i//10%10,3) + pow(i%10,3):
        print(i, "=", pow(i//100,3), "+", pow(i//10%10,3),"+",  pow(i%10,3))
print()
    
   
   
    
    
    
    
    
    
