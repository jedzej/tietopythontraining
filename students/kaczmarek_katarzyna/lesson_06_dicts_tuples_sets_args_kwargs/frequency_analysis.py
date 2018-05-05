def main():
    word_dict = {}
    for x in range(int(input("Number of lines: "))):
        for word in input("#" + str(x + 1) + " Line of text:").split():
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

    sorted_list = sorted([(-count, word) for word, count in word_dict.items()])
    for count, word in sorted_list:
        print(word)


if __name__ == '__main__':
    main()
