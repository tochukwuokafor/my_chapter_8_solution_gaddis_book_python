def main():
    enter_string = input('Please enter a string: ')
    answer = ''
    sentence_start = True
    for character in enter_string:
        if sentence_start == True:
            if character.isalpha():
                character = character.upper()
                sentence_start = False
            elif character.isdigit():
                sentence_start = False
        if character == '.' or character == '!' or character == '?':
            sentence_start = True
        answer += character

    print('The modified string is:', answer)
    
main()