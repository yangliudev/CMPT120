import pathlib

def print_max(ls):
    ls = ls.split(',')
    prev = -2 ** 32
    for num in ls:
        if float(num) > prev:
            prev = float(num)
    return prev

def main():
    file = open(str(pathlib.Path(__file__).parent.resolve()) + '/numbers.csv', 'r')

    for line in file:
        print(print_max(line))

main()
