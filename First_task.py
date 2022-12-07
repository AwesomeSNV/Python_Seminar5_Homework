#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

test_text = 'Напишите абвпрограмму, удаабвляющую из текста абвсе слова, содерабвжащие "абв".'
print(test_text)

def Delete_Words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

test_text = Delete_Words(test_text)
print(test_text)