def vowel_counter(string_entered):
    accumulator = 0
    for character in string_entered:
        if character.lower() in ['a', 'e', 'i', 'o', 'u']:
            accumulator += 1
    return accumulator

def consonant_counter(string_entered):
    counter = 0
    for character in string_entered:
        if character.lower() not in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter

def main():
    enter_string = input('Please enter a string: ')
    number_of_vowels = vowel_counter(enter_string)
    number_of_consonants = consonant_counter(enter_string)
    print('There are', number_of_vowels, 'vowels and', number_of_consonants, 'consonants in the string.')

main()