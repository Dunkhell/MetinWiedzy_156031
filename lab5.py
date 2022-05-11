import math
import random
import numpy as np

australian_dat = []

with open('australian.dat', 'r') as data:
    for line in data:
        # australian_dat.append([float(x) for x in line.split(' ')])
        australian_dat.append(list(map(lambda x: float(x), line.split(' '))))


# print(australian_dat)


# =============================================================================================================================
def metrykaEuk(x, y):
    wynik = 0
    for i in range(len(x)):
        wynik += math.pow(x[i] - y[i], 2)
    return math.sqrt(wynik)


def metryka_euklidesowa_skalar(l1, l2):
    v1 = np.array(l1)
    v2 = np.array(l2)
    a = v2 - v1
    return math.sqrt(np.dot(a, a))


def kolorowanie(array):
    array_with_new_rating = [entry[:14] + [float(random.randint(0, 1))] for entry in array]

    min_dist_dict = {}
    all_distances = {}

    made_changes = 0
    iter = 0

    while True:
        iter += 1
        for rating in range(2):
            for i in range(len(array_with_new_rating)):
                distance = 0
                if array_with_new_rating[i][-1] == rating:
                    for j in range(len(array_with_new_rating)):
                        if array_with_new_rating[j][-1] == rating:
                            distance += metrykaEuk(array_with_new_rating[i], array_with_new_rating[j])
                    all_distances[i] = distance
            min_dist = list(dict(sorted(all_distances.items(), key=lambda value: value[1])).keys())[0]
            min_dist_dict[rating] = min_dist
            all_distances = {}

        print(f'middle point: {min_dist_dict}')

        for rating in range(2):
            for i in range(len(array_with_new_rating)):

                if i in min_dist_dict.values():
                    continue

                if array_with_new_rating[i][-1] == rating:
                    current_dist = metrykaEuk(array_with_new_rating[min_dist_dict.get(rating)],
                                              array_with_new_rating[i])
                    dist_zero = metrykaEuk(array_with_new_rating[min_dist_dict.get(0)],
                                           array_with_new_rating[i])
                    dist_one = metrykaEuk(array_with_new_rating[min_dist_dict.get(1)],
                                          array_with_new_rating[i])
                    if current_dist > dist_one:
                        array_with_new_rating[i][-1] = float(1)
                        made_changes += 1
                    if current_dist > dist_zero:
                        array_with_new_rating[i][-1] = float(0)
                        made_changes += 1

        elements_one = 0
        elements_zero = 0

        for element in array_with_new_rating:
            if element[14] == 1.0:
                elements_one += 1
            if element[14] == 0.0:
                elements_zero += 1

        if str(iter) == "1":
            iter_string = str(iter) + "st"
        elif str(iter) == "2":
            iter_string = str(iter) + "nd"
        elif str(iter) == "3":
            iter_string = str(iter) + "rd"
        else:
            iter_string = str(iter) + "th"

        print(
            f'changes made in {iter_string} iteration {made_changes}\nelements with 0: {elements_zero} ||| elements with 1:{elements_one}')
        if made_changes == 0:
            break
        made_changes = 0

    return array_with_new_rating


# new_au_dat = kolorowanie(australian_dat)

def x_squared(x):
    return x ** x


def x(x):
    return x


def calculus_rectangle_method(n, function, end_x):
    sum = 0

    for i in range(1, n + 1):
        x_0 = end_x / n * (i - 1)
        x_1 = end_x / n * i
        y_0 = function(x_0)
        y_1 = function(x_1)
        average = (y_0 + y_1) / 2
        sum += average
    return sum / n


# print(calculus_rectangle_method(1, x, 1))
# print(calculus_rectangle_method(100, x, 1))
# print(calculus_rectangle_method(1000, x, 1))
# print(calculus_rectangle_method(10000, x, 1))


def average(array):
    array_len = len(array)
    ones = np.ones(array_len)
    return np.dot(array, ones) / array_len


def variance(array):
    average_result = average(array)
    sum = 0.0
    for x in array:
        sum += (x - average_result) ** 2
    return sum / len(array)


def variance_vector(array):
    v1 = np.array(array)
    v2 = np.array(average(array))
    result = v2 - v1
    return np.dot(result, result) / len(array)


def standard_deviation(array):
    return math.sqrt(variance_vector(array))


print(average([5, 5, 5, 5]))
print(average([1, 2, 3, 4, 5]))
print(average([1, 2]))

print(variance([1, 2, 3, 4, 5]))
print(variance_vector([1, 2, 3, 4, 5]))
print(standard_deviation([1, 2, 3, 4, 5]))


def metoda_ktora_zazwyczaj_nie_dziala(points):
    x_array = np.array([[1, x[0]] for x in points])
    y_array = np.array([y[1] for y in points])

    kov_matrix = np.dot(x_array.T, x_array)
    rev_matrix = np.linalg.inv(kov_matrix)
    left_rev_matrix = np.dot(rev_matrix, x_array.T)
    print(left_rev_matrix)
    return np.dot(left_rev_matrix, y_array)


print(metoda_ktora_zazwyczaj_nie_dziala([[2, 1], [5, 2], [7, 3], [8, 3]]))