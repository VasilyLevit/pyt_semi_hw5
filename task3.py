# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

in_str = 'Мы неабв очень любим Питон иабв Джавабв'
text_find = 'абв'
in_list = in_str.split()
# i = 0
# while i in range(len(in_list)):
#     if text_find in in_list[i]:
#         in_list.remove(in_list[i])
#     else:
#         i += 1
# print(in_list)

out_list = [item for item in in_list if text_find not in item]
print(out_list)