def main():
    message = input('Please enter a message you will like to encrypt: ')
    shift_amount = int(input('Kindly enter a shift amount: '))
    alphabet_dict = {'A': 1,
                    'B': 2,
                    'C': 3,
                    'D': 4,
                    'E': 5,
                    'F': 6,
                    'G': 7,
                    'H': 8,
                    'I': 9,
                    'J': 10,
                    'K': 11,
                    'L': 12,
                    'M': 13,
                    'N': 14,
                    'O': 15,
                    'P': 16,
                    'Q': 17,
                    'R': 18,
                    'S': 19,
                    'T': 20,
                    'U': 21,
                    'V': 22,
                    'W': 23,
                    'X': 24,
                    'Y': 25,
                    'Z': 26}
    return_upper = ''
    encrypted_message = ''
    for character in message:
        if character.islower():
            character = character.upper()
            return_upper += character
        elif character.isdigit():
            return_upper += character
        else:
            return_upper += character
    for letter in return_upper:
        if letter.isalpha():
            alphabet_number = alphabet_dict[letter]
            new_alphabet_number = alphabet_number + shift_amount
            if new_alphabet_number <= 26:
                for key, value in alphabet_dict.items():
                    if new_alphabet_number == value:
                        encrypted_message += key
            else:
                remainder = new_alphabet_number % 26
                for key, value in alphabet_dict.items():
                    if remainder == value:
                        encrypted_message += key
        elif letter.isdigit():
            encrypted_message += letter
        elif letter == '.' or letter == ' ' or letter == '!' or letter == '?':
            encrypted_message += letter
    print('The encrypted message is:', encrypted_message)

main()