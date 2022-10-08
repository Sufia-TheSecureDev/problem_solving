def wrap(string, max_width):
    substr = []
    for i in range(0, len(string), max_width):
        substr.append(string[i:i+max_width] )
    return '\n'.join(substr)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
