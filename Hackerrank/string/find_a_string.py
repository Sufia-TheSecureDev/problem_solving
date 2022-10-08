def count_substring(string, sub_string):
    total = 0
    sl = len(sub_string)
    for i in range(len(string)):
        if string[i:i+sl] == sub_string:
            total += 1
        else:
            continue
    return total
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
