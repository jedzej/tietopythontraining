def sort(func):
    def list_sort():
        return sorted(func())
    return list_sort


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print(data_feeder())


if __name__ == '__main__':
    main()
