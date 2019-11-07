def main():
    numbers = input('Enter a series of single-digit numbers with nothing separating them: ')
    accumulator = 0
    for number in numbers:
        number = int(number)
        accumulator += number
    print('The sum of all the single-digit numbers in the string is', accumulator)

main()