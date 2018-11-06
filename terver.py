import math
import operator
import matplotlib.pyplot as plt
from fractions import Fraction as f

#--------------------------------------------------------LIB-------------------------------------------------------------------


def drv(const):
    return {const: 1}


def print_drv_with_integer_keys(drv):
    print('{')
    for k, v in sorted(drv.items()):
        print(str(int(k)) + ': ' + str(v) + ',')
    print('}')


def operate_drv(first, second, keygen):
    result = {}
    for k1, v1 in first.items():
        for k2, v2 in second.items():
            key, value = keygen(k1, k2), v1 * v2
            if key in result.keys():
                result[key] += value
            else:
                result[key] = value
    return result


def multiply(first, second):
    return operate_drv(first, second, operator.mul)


def lcm_of_drv(first, second):
    return operate_drv(first, second, lcm)


def gcd_of_drv(first, second):
    return operate_drv(first, second, gcd)


def math_expect(drv):
    return sum([k * v for k, v in drv.items()])


def dispersion(drv):
    expectation = math_expect(drv)
    squared_drv = drv_pow(drv, 2)
    return math_expect(squared_drv) - expectation ** 2


def distribution_function(drv):
    current_probability = 0
    result = {}
    for key, value in sorted(drv.items()):
        current_probability += value
        result[key] = current_probability
    return result


def median(drv):
    distr_func = distribution_function(drv)
    for x in distr_func.keys():
        if distr_func[x] >= 0.5 and 1 - distr_func[x] + drv[x] >= 0.5:
            return x


def square_deviation(drv):
    return math.sqrt(dispersion(drv))


def covariation(first, second):
    return math_expect(multiply(first, second)) - math_expect(first) * math_expect(second)


def correlation(first, second):
    cov = covariation(first, second)
    dispersion1 = dispersion(first)
    dispersion2 = dispersion(second)
    return cov / math.sqrt(dispersion1 * dispersion2)


def drv_pow(drv, d):
    return {k**d: v for k, v in drv.items()}


def gcd(a, b):
    #Compute the greatest common divisor of a and b
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    #Compute the lowest common multiple of a and b
    return a * b / gcd(a, b)


#--------------------------------------------------------Домашняя работа №7-------------------------------------------------------------------
#Входные данные, две ДСВ - кси и эта.
#Найдем закон распределения ДСВ тэта.
кси = {1: f(1, 6), 2: f(1, 6), 3: f(1, 6), 4: f(1, 6), 5: f(1, 6), 6: f(1, 6)}
эта = {1: f(1, 12), 2: f(1, 12), 3: f(1, 3),
       4: f(1, 3), 5: f(1, 12), 6: f(1, 12)}
закон_распределения_ДСВ_Тэта = operate_drv(
    кси, эта, lambda x, y: lcm(x + 2, x * y))
#Выведем полученную ДСВ в консоль
print("Закон распределения случайной величины Тэта:")
print_drv_with_integer_keys(закон_распределения_ДСВ_Тэта)

#Пункт А) Нарисовать график

points = distribution_function(закон_распределения_ДСВ_Тэта)
plt.plot(points.keys(), points.values())
plt.title('Закон распределения случайной величины Тэта')
plt.ylabel('Вероятность')
plt.xlabel('Значение случайной величины')
plt.show()

#Пункт Б) Найти Матожидание
матожидание = math_expect(закон_распределения_ДСВ_Тэта)
print("Математическое ожидание случайной величины Тэта = " + str(матожидание))

#Пункт B) Найти дисперсию
дисперсия = dispersion(закон_распределения_ДСВ_Тэта)
print("Дисперсия случайной величины Тэта = " + str(дисперсия))

#--------------------------------------------------------Домашняя работа №8-------------------------------------------------------------------

#Задача №1
# Пункт А) Найти медиану
медиана = median(закон_распределения_ДСВ_Тэта)
print("Медиана случайной величины Тэта = " + str(медиана))

# Пункт Б) Найти среднеквадратичное отклонение
среднеквадратичное_отклонение = square_deviation(закон_распределения_ДСВ_Тэта)
print("Среднеквадратичное отклонение случайной величины Тэта = " +
      str(среднеквадратичное_отклонение))

#Задача №2
# Я выбрал случайную величину группы ФТ-302
закон_распределения_дсв_группы_КН_302 = operate_drv(кси, эта, lambda x, y: gcd(x * x, 3 * y))

# Пункт А) Найти ковариацию
ковариация = covariation(закон_распределения_ДСВ_Тэта,
                         закон_распределения_дсв_группы_КН_302)
print(
    "Ковариация случайных величин групп КН-301 и ФТ-302 = {0:.16f}".format(ковариация))

# Пункт Б) Найти корреляцию
корреляция = correlation(закон_распределения_ДСВ_Тэта,
                         закон_распределения_дсв_группы_КН_302)
print(
    "Корреляция случайных величин групп КН-301 и ФТ-302 = {0:.16f}".format(корреляция))
