def get_sum_of_digits():
    num = int(input())
    first_num = num // 100
    second_num = num // 10 % 10
    third_num = num % 10
    sum = first_num + second_num + third_num
    print('Sum of digit is {}'.format(sum))


if __name__ == '__main__':
    get_sum_of_digits()
