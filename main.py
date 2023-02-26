# 14.09.2022
# 1. Напишите программу на Python для чтения всего текстового файла.

# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file:
#     print(file.read())
#
# 2. Напишите программу на Python для чтения первых n строк файла.
# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file:
#     # print(file.readlines(1))
#     # print(file.readlines(2))
#     re = file.readlines()
#     for i in range(2):
#         print(re[i])

# 3. Напишите программу на Python для добавления текста в файл и отображения текста.
# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'w+', encoding="utf-8") as file:
#     file.write("Информация не имеет материи")
#
# txt = open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", encoding="utf-8")
# print(txt.read())
# txt.close()


# 4. Напишите программу на python, чтобы найти самые длинные слова.
# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file:
#     words = file.read().split()
#
# max_len = ''
# lm = 0
# for w in words:
#     l = len(w)
#     if l > lm:
#         max_len = w
#         lm = l
#
# print(max_len)


# 5. Напишите программу для подсчета количества строк в текстовом файле:
# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file:
#     str = file.readlines()
#     print(len(str))

# 6. Напишите программу на Python для подсчета частоты слов в файле.

# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file:
#     str = file.read().lower()
#     cher = ',.!?'
#     for ch in str:
#         if ch in cher:
#             str = str.replace(ch, '')
#     str = str.split()
#     print(str)
#     max_len = 0
#     maxWord = ""
#     for i in str:
#         n = 0
#         for j in str:
#             if j == i:
#                 n += 1
#         if n > max_len:
#             max_len = n
#             maxWord = i
# print("max = ", maxWord)

# 7. Напишите программу для записи списка в файл:
# with open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8") as file1, \
#         open("C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\copy.txt", 'w+', encoding="utf-8") as file2:
#     file2.write(file1.read())

# 8. Напишите программу для чтения случайной строки файла:
# with open('C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\test.txt", 'r', encoding="utf-8') as file:
#     arr_of_lines = file.readlines()
#     rand_ind = random.randint(1, len(arr_of_lines) - 1)
#     print(arr_of_lines[rand_ind])

# 9. Стоимость заказа
# Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# •	наименование товара;
# •	количество товара (целое число);
# •	цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.

# with open('C:\\Users\\Space\\OneDrive\\Рабочий стол\\333\\price.txt') as price_file:
#     products = price_file.read().split('\n')
#     summa = 0
#     for pr in products:
#         products = pr.split('\t')
#         summa += int(products[1]) * int(products[2])
#
#     print(summa)