import math

australian_dat = []

with open('australian.dat', 'r') as data:
    for line in data:
        # australian_dat.append([float(x) for x in line.split(' ')])
        australian_dat.append(list(map(lambda x: float(x), line.split(' '))))

print(australian_dat)


def euclid_metrics(list1, list2):
    result = 0

    if len(list1) != len(list2):
        return "Lists are different => Points have different dimensions"

    for i in range(len(list1) - 1):
        result += pow(list1[i] - list2[i], 2)

    return math.sqrt(result)


print(euclid_metrics(australian_dat[0], australian_dat[1]))
print(euclid_metrics(australian_dat[0], australian_dat[2]))
print(euclid_metrics(australian_dat[0], australian_dat[3]))


def grouped_rating(array, test_index, rating_index):
    if test_index == rating_index:
        return
    result = dict()
    element_under_test = array[test_index]
    for x in range(1, len(array)):
        rating = array[x][rating_index]
        if rating in result.keys():
            result[rating].append(euclid_metrics(element_under_test, array[x]))
        else:
            result[rating] = [euclid_metrics(element_under_test, array[x])]
    return result


print(grouped_rating(australian_dat, 0, 14))


def grouped_each(array):
    result = dict({1: [], 0: []})
    for i in range(len(array) - 1):
        for j in range(i, len(array) - 1):
            if array[i][len(array[0]) - 1] == 1:
                result[1].append(euclid_metrics(array[i], array[j]))
            else:
                result[0].append(euclid_metrics(array[i], array[j]))
    return result


print(grouped_each(australian_dat).get(0))
