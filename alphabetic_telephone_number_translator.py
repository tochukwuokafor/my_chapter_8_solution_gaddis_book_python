def main():
    telephone_number = input('Please enter a 10-character telephone number in the format XXX-XXX-XXXX: ')
    if telephone_number.islower():
        telephone_number = telephone_number.upper()
    telephone_number_list = list(telephone_number)
    for index, character in enumerate(telephone_number_list):
        if character in ['A', 'B', 'C']:
            telephone_number_list[index] = '2'
        if character in ['D', 'E', 'F']:
            telephone_number_list[index] = '3'
        if character in ['G', 'H', 'I']:
            telephone_number_list[index] = '4'
        if character in ['J', 'K', 'L']:
            telephone_number_list[index] = '5'
        if character in ['M', 'N', 'O']:
            telephone_number_list[index] = '6'
        if character in ['P', 'Q', 'R', 'S']:
            telephone_number_list[index] = '7'
        if character in ['T', 'U', 'V']:
            telephone_number_list[index] = '8'
        if character in ['W', 'X', 'Y', 'Z']:
            telephone_number_list[index] = '9'
    numeric_telephone_number = ''.join(telephone_number_list)
    print('The numeric equivalent of the phone number is', numeric_telephone_number)

main()