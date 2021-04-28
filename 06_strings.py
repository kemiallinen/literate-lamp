# sample_text = 'Baba bebe bobo bubu'
# new_sample_text = ''
# print(sample_text)
# # print('c' in sample_text)
#
# for letter in sample_text:
#     if letter == 'e':
#         new_sample_text += 'a'
#     else:
#         new_sample_text += letter   # new_sample_text = new_sample_text + letter
#
# print(new_sample_text)

sample_text = """baba bebe baba bebe baba bebe baba bebe baba bebe baba bebe
baba bebe baba bebe baba bebe baba bebe baba bebe baba bebe baba bebe baba
bebe baba bebe baba bebe baba bebe baba bebe baba bebe baba bebe baba bebe """
sample_text_list = list(sample_text)
print(sample_text_list)
sample_text_list[0] = 'ż'
sample_text = ''.join(sample_text_list)

print(sample_text.count('a'))
print(sample_text.replace('b', 'r'))
# print('' == ' ')
# print(len(''), len(' '))
#
# sample_list = ['a', 'b', 'c', 'd', 'e', ['f', 'g']]
#
# for i in range(len(sample_list)):
#     if type(sample_list[i]) == list:
#         sample_list.extend(sample_list[i])
#         sample_list.remove(sample_list[i])
#
# print(''.join(sample_list))
