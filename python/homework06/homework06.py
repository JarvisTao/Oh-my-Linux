#*****************************************
def laceString(s1, s2):

    s_lace = "" 
    len1 = len(s1)
    len2 = len(s2)

    for i in range(min(len1,len2)):
        s_lace += s1[i] 
        s_lace += s2[i]
    if len1 > len2:
        s_lace += s1[len2 : ]
    elif len2 > len1:
        s_lace += s2[len1 : ]
    
    return s_lace


if __name__ == "__main__":

    for i in range(3):
        s1 = input("Please input the 1st string: ")
        s2 = input("Please input the 2nd string: ")
        s_lace = laceString(s1, s2)
        print("s1 = {}\ns2 = {}".format(s1,s2))
        print("The laceString is {}.".format(s_lace))
        print()
