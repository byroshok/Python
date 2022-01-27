import math
# 1. Создать переменную item_1 типа integer.
item_1 = 7
#2. Создать переменную item_2 типа integer.
item_2 = 10
#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2
#  4. Вывести result_sum в консоль.
print(result_sum)
#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = item_2 - item_1
#  6. Вывести result_subtr в консоль.
print(result_subtr)
#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
result_multi = item_1 * item_2
#  8. Вывести result_multi в консоль.
print(result_multi)
#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2
#  10. Вывести result_exp в консоль.
print(result_exp)
#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1,item_2)
#  12. Вывести result_m_exp в консоль.
print(result_m_exp)
#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = math.sqrt(item_2)
# или так
result_s_root_1 = item_2 ** 0.5
#  14. Вывести result_s_root в консоль.
print(result_s_root)
print(result_s_root_1)
#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
#  16. Вывести result_m_s_root в консоль.
# готово в 13
#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_2,0.5)
#  18. Вывести result_mp_s_root в консоль.
print(result_mp_s_root)

#  19. Присвоить переменной item_1 odd значение
item_1_odd= 10
#  20. Присвоить переменной item_2 even значение
item_2_even= 50
#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division= item_1 / item_2
#  22. Вывести result_division в консоль.
print(result_division)
#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)
#  24. Вывести result_m_floor в консоль.
print(result_m_floor)
#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)
#  26. Вывести result_m_ceil в консоль.
print(result_m_ceil)
#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = round(math.ceil(result_division))
#  28. Вывести result_int в консоль.
print(result_int)
#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss =item_1 // item_2
#  30. Вывести result_no_division_loss в консоль.
print(result_no_division_loss)
#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
#  32. Вывести result_division_loss в консоль.
print(result_no_division_loss)
#
# Дальше будет реализация через арифметические действия с присваиванием.
#
#  33. Создать переменную item_3 и присвоить ей целое число
item_3 = int(8)
#  34. Прибавить 10 к item_3 с присвоением.
item_3 = item_3 +10
#  35. Вывести item_3 в консоль.
print(item_3)
#  36. Отнять 5 от item_3 с присвоением.
item_3 = item_3 - 5
#  37. Вывести item_3 в консоль.
print(item_3)
#  38. Умножить item_3 на 3 с присвоением.
item_3 = item_3 * 3
#  39. Вывести item_3 в консоль.
print(item_3)
#  40. Разделить item_3 на 2 с присвоением.
item_3 = item_3 / 2
#  41. Вывести item_3 в консоль.
print(item_3)
#  42. Возвести в степень 2 item_3 с присвоением.
item_3 = item_3 ** 2
#  43. Вывести item_3 в консоль.
print(item_3)
#  44. Найти квадратный корень item_3 с присвоением.
item_3 = int(math.sqrt(item_3))
#  45. Вывести item_3 в консоль.
print(item_3)
#  46. Присвоить остаток от деления item_3
item_3_mod = item_3 % 5
item_3 = item_3_mod + item_3
#  47. Вывести item_3 в консоль.
print(item_3)
#
# Boolean
#
#  48. Создать переменную b_item_t и присвоить True
b_item_t = True
#  49. Создать переменную b_item_f и присвоить False
b_item_f = False
#  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_relult = b_item_t + b_item_f
#  51. Вывести b_item_relult_sum в консоль.
print(b_item_relult)
#  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_relult_subtr =b_item_t - b_item_f
#  53. Вывести b_item_relult_subtr в консоль.
print(b_item_relult_subtr)
#  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_relult_multi = b_item_t * b_item_f
#  55. Вывести b_item_relult_multi в консоль.
print(b_item_relult_multi)
#  56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
# b_item_relult_division = b_item_t / b_item_f
#  57. Вывести b_item_relult_division в консоль. (Получить ошибку)
# print(b_item_relult_division)
#  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)
#  59. Вывести b_item_1_int в консоль.
print(b_item_1_int)
#  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
b_item_2 = False
b_item_2_int = int(b_item_2)
#  61. Вывести b_item_2_int в консоль.
print(b_item_2_int)
# Python HW 3 if else elif

#  1. Создать переменную int_item со значением 10
int_item = 10
#  2. Создать переменную comp_item со значением 18
comp_item = 18
#  3. Создать переменную mult_int в которй умножите int_item на 2
mult_int = int_item * 2
#  4. Создать переменную item_2 со значением True
item_2 = True
#  5. Создать переменную item_3 со значением False
item_3 = False
#  6. Создать переменную item_4 со значением 0
item_4 = 0
#  7. Создать переменную item_5 со значением 1
item_5 = 1
#  8. Создать переменную usd_item со значением ‘usd’
usd_item = 'usd'
#  9. Создать переменную usd_usd_rate со значением 1
usd_usd_rate = 1
#  10. Создать переменную eur_item со значением ‘eur’
eur_item = 'eur'
#  11. Создать переменную usd_eur_rate со значением 0.86
usd_eur_rate = 0.86
#  12. Создать переменную uah_item со значением ‘uah’
uah_item = 'uah'
#  13. Создать переменную usd_uah_rate со значением 26.23
usd_uah_rate = 26.23
#  14. Создать переменную chf_item со значением ‘chf’
chf_item = 'chf'
#  15. Создать переменную usd_chf_rate со значением 0.91
usd_chf_rate = 0.91
#  16. Создать переменную rub_item со значением ‘rub’
rub_item = 'rub'
#  17. Создать переменную usd_rub_rate со значением 71.88
usd_rub_rate = 71.88
#  18. Создать переменную byn_item со значением ‘byn’
byn_item = 'byn'
#  19. Создать переменную usd_byn_rate со значением 2.46
usd_byn_rate = 2.46
#  20. Сделать if в котором будет условие: если mult_int больше comp_item, то вывести в консоль (“Переменная mult_int больше”, comp_item)
if mult_int > comp_item:
    print('Переменная mult_int больше', comp_item)
#  21. Создать переменную div_int в которй разделить int_item на 2
div_int = int_item / 2
#  22. Сделать if в котором будет условие: если div_int меньше comp_item, то вывести в консоль (“Переменная div_int меньше”, comp_item)
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)
#  23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
item_1 = int_item + 10
#  24. Сделать if в котором будет условие: если item_1 меньше comp_item, то вывести в консоль (“Переменная item_1 меньше”, comp_item), иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
if int_item < comp_item:
    print('Переменная item_1 меньше', comp_item)
#  25. Сделать if в котором будет условие: если item_2, то вывести в консоль (“Переменная item_2 = ”, item_2), иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
if item_2:
    print('Переменная item_2 = ', item_2)
else: print('Переменная item_2 = ', item_3)
#  26. Сделать if в котором будет условие: если item_3, то вывести в консоль (“Переменная item_3 = ”, item_2), иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
if item_3:
    print('Переменная item_3 =', item_2)
else:
    print('Переменная item_3 = ', item_3)
#  27. Сделать if в котором будет условие: если item_5, то вывести в консоль (“Переменная item_5 = ”, item_5), иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
if item_5:
    print('Переменная item_5 =', item_5)
else:
    print('Переменная item_5 = ', item_4)
#  28. Сделать if в котором будет условие: если item_4, то вывести в консоль (“Переменная item_4 = ”, item_5), иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
if item_4:
    print('Переменная item_4 =', item_5)
else:
    print('Переменная item_4 = ', item_4)
#  29. Создать переменную currency_convertor со значением item_2
currency_convertor = item_2
#  30. Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания, иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
#  31. Внутри if currency_convertor сделать следующие If условия :
#  31.1 Создать переменную currency_usd со значением usd_item
#  31.2 Создать переменную target_currency со значением eur_item
#  31.3 Создать переменную target_currency_amount значением 50
#  31.4 Создать переменную currency_result со значением 0
#  31.4 Сделать if в котором будет условие: если target_currency равен ‘eur’, то в теле этого if в        значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_eur_rate. Результат вывести в консоль (target_currency_amount, eur_item, “=”, currency_result, usd_item)
#  31.5 Сделать elif в котором будет условие: если target_currency равен ‘uah’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_uah_rate. Результат вывести в консоль (target_currency_amount, uah_item, “=”, currency_result, uah_item)
#  31.6 Сделать elif с остальными валютами
#  31.7 Последним оставить else, при выполнений которого в консоль выведется (“Unknow currency”)
if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == 'eur':
        currency_result = target_currency_amount * usd_eur_rate
        print(target_currency_amount, eur_item, '=', currency_result, usd_item)
    elif target_currency == 'uah':
        currency_result = target_currency_amount * usd_uah_rate
        print(target_currency_amount, uah_item, '=', currency_result, uah_item)
    else:
        print('Переменная currency_convertor = ', item_3)
    if target_currency == 'usd':
        currency_result = target_currency_amount * usd_usd_rate
        print(target_currency_amount, usd_item, '=', currency_result, usd_item)
    elif target_currency == 'chf':
        currency_result = target_currency_amount * usd_chf_rate
        print(target_currency_amount, chf_item, '=', currency_result, chf_item)
    elif target_currency == 'rub':
        currency_result = target_currency_amount * usd_rub_rate
        print(target_currency_amount, rub_item, '=', currency_result, rub_item)
    elif target_currency == 'byn':
        currency_result = target_currency_amount * usd_byn_rate
        print(target_currency_amount, byn_item, '=', currency_result, byn_item)
    else:
        print('Unknow currency')
