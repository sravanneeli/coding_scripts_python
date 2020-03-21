def maxset(A):
    n = len(A)
    i = 0
    temp = []
    sub_array_list = []
    while i < len(A):
        if A[i] < 0:
            sub_array_list.append(temp)
            temp = []
            i += 1
        else:
            temp.append(A[i])
            i += 1
    sub_array_list.append(temp)
    sum_sub = [0] * len(sub_array_list)
    for i, sub in enumerate(sub_array_list):
        sum_sub[i] = sum(sub)
    max_sum = max(sum_sub)
    max_sub = []
    for sub in sub_array_list:
        if sum(sub) == max_sum:
            max_sub.append(sub)
    if len(max_sub) == 1:
        return max_sub[0]
    else:
        maxList = max(x for x in max_sub)
        return maxList


def main():
    print(maxset([0, 0, -1, 0]))


if __name__ == "__main__":
    main()
