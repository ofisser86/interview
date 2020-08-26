def catalan_number(num):
    if num <= 1:
        return 1

    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num - i - 1)
    return res_num


if __name__ == '__main__':
    pairs_of_brackets = int(input("Enter amount pairs sof brackets --> "))
    print(catalan_number(pairs_of_brackets))
