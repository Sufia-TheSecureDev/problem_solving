if __name__ == '__main__':
    s = input()
    for opr in ['alnum', 'alpha', 'digit', 'lower', 'upper']:
        print(any([eval(f'char.is{opr}()') for char in s]))
