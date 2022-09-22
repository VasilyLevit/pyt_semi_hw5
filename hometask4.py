# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

in_data = 'aaabccdd'
# do input from file in future

encoding = []
i = 0
while i < len(in_data):
    count = 1
    while i + 1 < len(in_data) and in_data[i] == in_data[i + 1]:
            count += 1
            i += 1
    encoding.append(str(count) + in_data[i])
    i += 1

print(encoding)

# do codding metod