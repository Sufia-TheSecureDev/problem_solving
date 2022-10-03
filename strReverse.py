def reverse(s):
    str = ""
    for i in s:
        str =  i + str
    return str
 
s = input()
r =reverse(s) 
if s == r :
    print('Palindrome')
else:
    print('not palindrome')
