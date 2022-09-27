# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# coding metod
in_data = 'aaabccdd'

coding = []
i = 0
while i < len(in_data):
    count = 1
    while i + 1 < len(in_data) and in_data[i] == in_data[i + 1]:
            count += 1
            i += 1
    coding.append(str(count) + in_data[i])
    i += 1

with open('coding.txt', 'w') as data:
    data.write("".join(coding))


# encoding metod
# path = 'C:\Users\vasil\OneDrive\ProjectProg\Python\GBtask\seminar5\in_string.txt'
f = open('coding.txt', 'r')
s_input = f.read()
f.close()

s_output = []
s_input = list(filter(lambda x: int(x) if x.isdigit() else x, s_input))

for i in s_input:
    if i.isdigit():
        tmp_mult = int(i)
    else:
        s_output.append(i * tmp_mult)

with open('encoding.txt', 'w') as data:
    data.write("".join(s_output))
