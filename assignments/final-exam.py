# Final Exam

def translate(phone_number):
    phone_letters = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
                     'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
                     'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
                     'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
                     'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
                     'Z': '9'}

    translated_number = ''
    for i in phone_number:
        if i.isalpha():
            translated_number += phone_letters[i.upper()]
        else:
            translated_number += i
    return translated_number


def response(translated_number):
    print('The translated phone number is:', translated_number)


def main():
    # get input from user
    phone_number = input('Enter a phone number to be translated:')

    # translate the phone number
    translated_number = translate(phone_number)
    # print response
    response(translated_number)


main()
