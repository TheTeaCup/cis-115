# Random Number File Reader
# Chapter 6 | Programming Exercise 8


def main():
    file = open('random-number-file.txt', 'r')
    read(file)


def read(file):
    longest_word = ""
    word_count = 0
    total_length = 0
    for line in file:
        arr = line.split()
        for word in arr:
            total_length = total_length + len(word)
            if len(word) > len(longest_word):
                longest_word = word
            word_count = word_count + 1

    avg_length = total_length / word_count
    print("Number of words:", word_count)
    print("Longest word:", longest_word)
    print("Average word length:", avg_length)


main()
