def main():
    enter_string = input('Please enter a string: ')
    character_dict = {}
    for character in enter_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    values = [value for value in character_dict.values()]
    maximum_frequency = max(values)
    # if there is only character that appears most frequently ...
    if list(character_dict.values()).count(maximum_frequency) == 1:
        for char, val in character_dict. items():
            if val == maximum_frequency:
                print('The character that appears most frequently in the string is', char)
    # if there is a tie of most frequently occurring characters ...
    else:
        char_list = [char for char, val in character_dict.items() if val == maximum_frequency ]
        print('The characters that appear most frequently in the string are', char_list)

main()