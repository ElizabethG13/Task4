"Проверка на число)) "
def number_check(num):
    try:
        float(num)
        return True
    except ValueError:
        raise SystemExit("Ошибка. Неверное число.")
        return False


print("Введите первое число: ")

a = input()
number_check(a)

print("Введите второе число: ")
b = input()
number_check(b)

print("Введите оператор: ")
oper = input()
static_oper = frozenset({'+', '-', '/', '*', '//', '**', '%'})

if oper not in static_oper:
    raise SystemExit("Ошибка. Несуществующий оператор.")

expression = a+oper+b
print("Ответ: ", str(eval(expression)))