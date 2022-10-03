from curses.ascii import isdigit, islower, isupper

upperLetter = ''
lowerLetter = ''
digit = ''
others = ''

str =  input()
for s in str:
    if isupper(s):
        upperLetter += s
    elif islower(s):
        lowerLetter += s
    elif isdigit(s):
        digit += s
    else:
        others += s 

print(upperLetter , lowerLetter, digit , others)
