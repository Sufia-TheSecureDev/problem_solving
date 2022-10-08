def solve(s): 
    cap =[]
    for i in s.split(' '):
        cap.append(i.capitalize() )
    return ' '.join(cap)
s = input()
result = solve(s)
print(result)
