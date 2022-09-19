# Задача1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось уловие A[i] - 1 = A[i-1]
# Найдите это число.

# with open('file51.txt','w') as data:
#     data.write('1 2 3 4 6 7 8 9')

data = open('file51.txt','r')
line_data = data.read()
data.close()

in_list = line_data.split()
print(in_list)

for i in range(1, len(in_list)):
    if int(in_list[i])-1 != int(in_list[i-1]):
        out_num = int(in_list[i])-1

print(out_num)