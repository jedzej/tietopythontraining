def get_adults_avg(list_of_ages):
    adults = [i for i in list_of_ages if i >= 18]
    if len(adults) != 0:
        return sum(adults) / len(adults)
    return 0


def get_amount_of_children(list_of_ages):
    return len([i for i in list_of_ages if i < 18])


if __name__ == '__main__':
    list_of_ages = [int(s) for s in input().split()]
    print("Average age adults is: " + str(get_adults_avg(list_of_ages)))
    print("Amount of children is: " + str(get_amount_of_children(list_of_ages)))
