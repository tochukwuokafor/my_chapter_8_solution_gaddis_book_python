def main():
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    print(first_name[0].upper() + '.' + last_name[0].upper() + '.')
    print(first_name.capitalize(), last_name.upper())
    print(first_name[0].lower() + last_name.lower())

main()