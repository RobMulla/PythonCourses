# Problem 2 - counting bobs
# This program that prints the number of times 
# the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print


length = len(s)
count = 0
for x in range(0,length-2):
    if s[x] == 'b' and s[x+1] == 'o' and s[x+2] == 'b':
        count += 1

print("Number of times bob occurs is: " + str(count))
