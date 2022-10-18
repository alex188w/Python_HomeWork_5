# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

with open('RLE_decoded.txt', 'r') as data:
    my_text = data.read()
print(f'Строка до кодирования: {my_text}')


def encode_rle(ss):
    str_encoding = ''
    prev_char = ''
    count = 1

    if not ss:
        return ''

    for char in ss:
        if char != prev_char:
            if prev_char:
                str_encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    else:
        str_encoding += str(count) + prev_char

    return str_encoding


str_encoding = encode_rle(my_text)
print(f'Строка после кодирования: {str_encoding}')


with open('RLE_encoded.txt', 'r') as data:
    my_text2 = data.read()
print(f'Закодированная сжатая строка: {my_text2}')


def decoding_rle(ss):
    str_decode = ''
    count = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(f'Строка после декодирования: {str_decode}')
