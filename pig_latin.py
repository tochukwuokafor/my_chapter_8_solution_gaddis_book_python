def main():
    enter_sentence = input('Please enter a sentence: ')
    sentence_caps = ''
    ADDITIONAL_STR = 'AY'
    for character in enter_sentence:
        if character.isupper():
            sentence_caps += character
        else:
            character = character.upper()
            sentence_caps += character
    sentence_list = sentence_caps.split()
    for index, item in enumerate(sentence_list):
        fix_at_end = item[1:] + item[0] + ADDITIONAL_STR
        sentence_list[index] = fix_at_end
    pig_latin = ' '.join(sentence_list)
    print(pig_latin)

main()