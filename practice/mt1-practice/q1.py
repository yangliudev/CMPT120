def print_max(ls):
    prev = -2 ** 32
    for num in ls:
        if num > prev:
            prev = num
    print(prev)

def main():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    num3 = int(input('Enter a number: '))
    num4 = int(input('Enter a number: '))
    num5 = int(input('Enter a number: '))
    ls = [num1, num2, num3, num4, num5]
    print_max(ls)

main()
