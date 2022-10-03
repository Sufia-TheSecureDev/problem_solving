newStr = ''
str = input()
for i in range(0 , len(str) , 2):
    newStr += str[i+1] + str[i]

print(newStr)
