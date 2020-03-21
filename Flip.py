def flip(A):
    max_sum = 0
    summ = 0
    start = 0
    ans = None
    for i, a in enumerate(A):
        summ += (1 if a is '0' else -1)
        if summ < 0:
            summ = 0
            start = i + 1
            continue
        if summ > max_sum:
            max_sum = summ
            ans = [start, i]
    if ans is None:
        return []
    return list(map(lambda x: x+1, ans))


def main():
    print(flip("0100"))


if __name__ == '__main__':
    main()
