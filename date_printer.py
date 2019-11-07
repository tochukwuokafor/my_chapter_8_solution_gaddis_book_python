def main():
    enter_date = input('Please enter date in the format mm/dd/yyyy: ')
    date_part_list = enter_date.split('/')
    month_dict = {1: 'January', 2: 'February', 3: 'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    print('The new date format is ' + month_dict[int(date_part_list[0])] + ' ' + date_part_list[1] + ', ' + date_part_list[2])

main()