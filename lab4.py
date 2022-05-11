import random as rand


def montecarlo(foo, foo2, fx, lx, eps):
    original = foo2(lx) - foo2(fx)
    done = 0
    points = 1000
    ile = 0
    minimum, maximum = foo(fx), foo(lx)
    random = []
    ile = 0
    # print(minimum,maximum)
    while abs(done - original) > eps:
        points += 1000
        for i in range(1000):
            new_x = rand.uniform(fx, lx)
            new_y = rand.uniform(minimum, maximum)
            while (new_x, new_y) in random:
                new_x = rand.uniform(fx, lx)
                new_y = rand.uniform(minimum, maximum)
            random.append((new_x, new_y))

            result = foo(new_x)
            if new_y <= result:
                ile += 1
        done = (lx - fx) * (maximum - minimum) * (ile / points)
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} punktów:{1}. Rzeczywiste: {2}".format(points,
                                                                                                               done,
                                                                                                               original,
                                                                                                               eps))
    return done


def f2(x):
    return x ** 2 / 2


def f(x):
    return x


# aproksymacją dolną
def rectangle(foo, foo2, fx, lx, eps):
    original = foo2(lx) - foo2(fx)
    done = 0
    divider = 1
    distance = 1
    while abs(done - original) > eps:
        done = 0
        divider *= 2
        distance = float(lx - fx) / float(divider)
        for i in range(divider):
            done += foo(fx + distance * i) * distance
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(
            divider, done, original, eps))
    return done


# aproksymacją górną
def rectangle2(foo, foo2, fx, lx, eps):
    original = foo2(lx) - foo2(fx)
    done = 0
    divider = 1
    distance = 1
    while abs(done - original) > eps:
        done = 0
        divider *= 2
        distance = float(lx - fx) / float(divider)
        for i in range(1, divider + 1):
            done += foo(fx + distance * i) * distance
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(
            divider, done, original, eps))
    return done


# aproksymacją srednia
def rectangle3(foo, foo2, fx, lx, eps):
    original = foo2(lx) - foo2(fx)
    done = 0
    lower = 0
    upper = 0
    divider = 1
    distance = 1
    while abs(done - original) > eps:
        done = 0
        divider *= 2
        distance = float(lx - fx) / float(divider)
        for i in range(1, divider + 1):
            lower = foo(fx + distance * (i - 1)) * distance
            upper = foo(fx + distance * i) * distance
            done += (lower + upper) / 2
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(
            divider, done, original, eps))
    return done


print(montecarlo(f, f2, 0, 1, 0.05))
print(rectangle(f, f2, 0, 1, 0.01))
print(rectangle2(f, f2, 0, 1, 0.01))
print(rectangle3(f, f2, 0, 1, 0.01))
