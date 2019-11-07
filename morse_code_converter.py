def main():
    enter_string = input('Please enter a string that you would like to convert to Morse code: ')
    enter_string = enter_string.upper()
    enter_string_list = list(enter_string)
    for index, character in enumerate(enter_string_list):
        if character == ' ':
            enter_string_list[index] = ' '
        if character == ',':
            enter_string_list[index] = '--..--'
        if character == '.':
            enter_string_list[index] = '.-.-.-'
        if character == '?':
            enter_string_list[index] = '..--..'
        if character == '0':
            enter_string_list[index] = '-----'
        if character == '1':
            enter_string_list[index] = '.----'
        if character == '2':
            enter_string_list[index] = '..---'
        if character == '3':
            enter_string_list[index] = '...--'
        if character == '4':
            enter_string_list[index] = '....-'
        if character == '5':
            enter_string_list[index] = '.....'
        if character == '6':
            enter_string_list[index] = '-....'
        if character == '7':
            enter_string_list[index] = '--...'
        if character == '8':
            enter_string_list[index] = '---..'
        if character == '9':
            enter_string_list[index] = '----.'
        if character == 'A':
            enter_string_list[index] = '.-'
        if character == 'B':
            enter_string_list[index] = '-...'
        if character == 'C':
            enter_string_list[index] = '-.-.'
        if character == 'D':
            enter_string_list[index] = '-..'
        if character == 'E':
            enter_string_list[index] = '.'
        if character == 'F':
            enter_string_list[index] = '..-.'
        if character == 'G':
            enter_string_list[index] = '--.'
        if character == 'H':
            enter_string_list[index] = '....'
        if character == 'I':
            enter_string_list[index] = '..'
        if character == 'J':
            enter_string_list[index] = '.---'
        if character == 'K':
            enter_string_list[index] = '-.-'
        if character == 'L':
            enter_string_list[index] = '.-..'
        if character == 'M':
            enter_string_list[index] = '--'
        if character == 'N':
            enter_string_list[index] = '-.'
        if character == 'O':
            enter_string_list[index] = '---'
        if character == 'P':
            enter_string_list[index] = '.--.'
        if character == 'Q':
            enter_string_list[index] = '--.-'
        if character == 'R':
            enter_string_list[index] = '.-.'
        if character == 'S':
            enter_string_list[index] = '...'
        if character == 'T':
            enter_string_list[index] = '-'
        if character == 'U':
            enter_string_list[index] = '..-'
        if character == 'V':
            enter_string_list[index] = '...-'
        if character == 'W':
            enter_string_list[index] = '.--'
        if character == 'X':
            enter_string_list[index] = '-..-'
        if character == 'Y':
            enter_string_list[index] = '-.-'
        if character == 'Z':
            enter_string_list[index] = '--..'
    morse_code = ''.join(enter_string_list)
    print('The Morse code is', morse_code)

main()