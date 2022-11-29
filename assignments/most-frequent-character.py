# Most Frequent Character
# Chapter 8 | Programming Exercise 10


def main():
    string = input('Please input a string: ')

    value = processing(string)  # get the most frequent letter then share it to response
    response(value)


def processing(string):
    count = 0
    total_count = 0
    most_frequent_letters = ""

    for ch in string:
        for stri in string:
            if stri == ch:
                count += 1
        if count > total_count:
            total_count = count
        count = 0

    # Finding most frequent letter using count
    for ch in string:
        for stri in string:
            if stri == ch:
                count += 1
        if count == total_count:
            if ch not in most_frequent_letters:
                most_frequent_letters += ch
        count = 0
    return most_frequent_letters  # return the most frequent letter


def response(value):
    print('The most frequently occurring letter(s):', value)


main()
