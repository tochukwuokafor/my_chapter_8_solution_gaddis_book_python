def main():
    enter_string = input('Please enter a sentence in which all of the words are run together, but the first character of each word is uppercase: ')
    answer = ''
    sentence_start = True
    for character in enter_string:
        if sentence_start == True:
            if character.isdigit():
                answer += character
                sentence_start = False
            if character.isupper():
                answer += character
                sentence_start = False
        else:
            if character.isdigit():
                character = ' ' + character
                answer += character
            elif character.islower():
                answer += character
            elif character.isupper():
                character = ' ' + character.lower()
                answer += character
            else:
                answer += character
    print('The modified string is:', answer)

main()