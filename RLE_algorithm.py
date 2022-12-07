# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE_input.txt', 'r') as data:
    text = data.read()

def Compression_RLE(st):
    str_code = ''
    prev_element = ''
    count = 1
    for element in st:
        if element != prev_element:
            if prev_element:
                str_code += str(count) + prev_element
            count = 1
            prev_element = element
        else:
            count += 1
    return str_code

str_com = Compression_RLE(text)
print(str_com)

with open('RLE_compressed.txt', 'r') as data:
    second_text = data.read()

def Recovery_RLE(st:str):
    count = ''
    str_decode = ''
    for element in st:
        if element.isdigit():
            count += element
        else:
            str_decode += element * int(count)
            count = ''
    return str_decode

str_recov = Recovery_RLE(second_text)
print(str_recov)