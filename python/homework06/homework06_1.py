#*************************************************
cnt = 0
for i in range(101):
	if i % 7 != 0:
		print("{:>4}".format(i),end = "")
		cnt += 1
	if cnt ==10:
		print()
		cnt = 0
		

#*************************************************
print()
import re
s = "azcbobobegghakl"
#s = "abcbcd"
s_find = "0"
for i in range(len(s)-1):
	if s[i + 1] >= s[i]:
		s_find = s_find + str(int(s_find[i])^0)
	else:
		s_find = s_find + str(int(s_find[i])^1)
print(s)
print(s_find)
print()
match_0 = re.findall(r'0+',s_find)
match_1 = re.findall(r'1+',s_find)

max_temp = max(match_0 + match_1, key = len)

pos = s_find.find(max_temp)
s_sub = s[pos : pos + len(max_temp)]
print("The longest substring in alphabetical order is:", s_sub)

#*************************************************
print()
s = "aa000 bb-c"
match = re.findall(r'\w+', s)
print("".join(match))

#******************************

