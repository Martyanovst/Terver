import operator
import matplotlib.pyplot as plt
from fractions import Fraction as f


def print_drv_with_integer_keys(drv):
    print('{')
    for k,v in drv.items():
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

def math_expect(drv):
    return sum([k * v for k, v in drv.items()])

def dispersion(drv):
    expectation = math_expect(drv)
    squared_drv = drv_pow(drv, 2)
    return math_expect(squared_drv) - expectation ** 2


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


#Входные данные, две ДСВ - кси и эта.
#Найдем закон распределения ДСВ тэта.
кси = {1: f(1, 6), 2: f(1, 6), 3: f(1, 6), 4: f(1, 6), 5: f(1, 6), 6: f(1, 6)}
эта = {1: f(1, 12), 2: f(1, 12), 3: f(1, 3), 4: f(1, 3), 5: f(1, 12), 6: f(1, 12)}
кси_плюс_2 = {k+2: v for k, v in кси.items()}
эта_умножить_на_кси = multiply(кси, эта)
закон_распределения_ДСВ_Тэта = lcm_of_drv(кси_плюс_2, эта_умножить_на_кси)
#Выведем полученную ДСВ в консоль
print("Закон распределения случайной величины Тэта:")
print_drv_with_integer_keys(закон_распределения_ДСВ_Тэта)

#Пункт А) Нарисовать график
items = закон_распределения_ДСВ_Тэта.items()
keys = [k for k, v in items]
values = [v for k, v in items]
plt.plot(keys, values, 'ro')
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

print_drv_with_integer_keys(эта)
print_drv_with_integer_keys(кси)
print(sum(закон_распределения_ДСВ_Тэта.values()))