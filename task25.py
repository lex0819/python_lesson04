# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

input_string = "a a a b c a a d c d d"
print(input_string)
split_string = input_string.split()
set_of_items = set(split_string) #key of dictionary
#print(set_of_items)
our_dict = dict.fromkeys(set_of_items, -1) #create dictionary
#print(our_dict)

output_string = [] #output list
for char in split_string:
    our_dict[char] += 1
    
    if our_dict[char] > 0:
        output_string.append(f"{char}_{our_dict[char]}")
    else:
        output_string.append(char)

output_text = ' '.join(output_string) #convert list to string devided by space
print("take the result:")
print(output_text)
print(*output_string) # * is unpacking 