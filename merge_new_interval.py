def insert(intervals, newinterval):
    intervals.append(newinterval)
    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = max(intervals[i][1], output[-1][1])
        else:
            output.append(intervals[i])
    return output


def main():
    new_list = insert([[1, 2], [3, 5], [3, 7]], [8, 10])
    print("New intervals after merging", new_list)


if __name__ == "__main__":
    main()
