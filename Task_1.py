# Напишите программу, удаляющую из текста все слова, содержащие ""абв""


my_text = 'Сегодня Сегабводня хорошаяабв хорошая погода абв'
print('Исходный тект: ')
print(my_text)

def del_word(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

my_text = del_word(my_text)
print('Текст после форматирования: ')
print(my_text)