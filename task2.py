# Дан список чисел. Создайте список, в который попадают числа, описывающие 
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

in_list = [1, 5, 2, 3, 4, 6, 1, 7]
out_list = [in_list[0]]
count = 0
for i in range(1, len(in_list)):
    if in_list[i] > in_list[count]:
        out_list.append(in_list[i])
        count = i
print(out_list)

# out_list =[in_list[i] for i in range(1, len(in_list)) if in_list[i] >= max(my_list[0:i]) ]
# out_list.insert(0, mylist[0])