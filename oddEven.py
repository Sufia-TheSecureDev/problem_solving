n = int(input())

if n  == 0 :
    print("Zero")
else:
    if n%2 == 1:
        print("Odd")
    else:
        if n >= 2 and n<=5 :
            print("even between 2 and 5")
        elif n >= 6 and n<=20 :
            print("even between 6 and 20")
        else:
            print("even greater than 20")