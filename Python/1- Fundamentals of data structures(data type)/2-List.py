# List  [  ]               in C = array
# mutable (se poate modifica),  orderd, [indexing, slicing, methods] , [index0, index1, index2, ...]
# can contain different data types
# can contain duplicates
# can contain other lists (nested lists)

my_list = [0, 1, 2, 3, 4, 5]  # list of integers
print(my_list [3])

names = ["mamal", "shadi", "sina", "sara"]  # list of strings
print(names[1])  # shadi
print(names[-1])  # sara
print(names[1:3])  # ['shadi', 'sina']
print(names[2:])  # ['sina', 'sara']
print(names[:3])  # ['mamal', 'shadi', 'sina']


Lists_2 = [1, 2, "man", 3.14, True, [1, 2, 3]]  # list with different data types
L = len(Lists_2)  # length of the list
print(L)  # 6


Lists_3 = [0, 1, 2, 3, 4, 5]
lenght = len(Lists_3)  # length of the list,  len count from 1
print(lenght)  # 6


new_list = my_list + names  # concatenation of two lists
print(new_list)  # [0, 1, 2, 3, 4, 5, 'mamal', 'shadi', 'sina', 'sara']
new_list2 = my_list * 2  # repetition of the list
print(new_list2)  # [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]

print(names.sort())  # sort the list in ascending order
print(new_list2.count(3))  # count the number of occurrences of an item in the list
new_list.append("new item")  # add new item to the end of the list
print(new_list)  # [0, 1, 2, 3, 4, 5, 'mamal', 'shadi', 'sina', 'sara', 'new item']
new_list.insert(0, "first item")  # insert new item at the beginning of the list
print(new_list)  # ['first item', 0, 1, 2, 3, 4, 5, 'mamal', 'shadi', 'sina', 'sara', 'new item']
new_list.remove("new item")  # remove item from the list


names = ["mamal", "shadi", "leila", "sara", "bita"]
last_names = names.pop()  # remove the last item from the list
print(last_names)  # bita
print(names)  # ['mamal', 'shadi', 'leila', 'sara']
names.sort()  # sort the list in ascending order
print(names)  # ['leila', 'mamal', 'sara', 'shadi']
names.reverse()  # reverse the order of the list
print(names)  # ['shadi', 'sara', 'mamal', 'leila']

print("__" * 20)

names2 = ["mamal", "shadi", "sina", "sara", "pooya"]

names2.append("new item")  # add new item to the end of the list
print(names2)  # ['mamal', 'shadi', 'sina', 'sara', 'pooya', 'new item']

names2.pop(2)  # remove item at index 2
print(names2)  # ['mamal', 'shadi', 'sara', 'pooya']

names2.remove("sara")  # remove item by value
print(names2)  # ['mamal', 'shadi', 'pooya']


llll= [1, 2, 3, 4, 5]
m = llll.index(3)  # find the index of the item
print(m)  # 2
n = llll[3] # get the item at index 3
print(n)


my_list_jadi = [1, 2, 3, 4, 5]
my_list_jadi.remove(3)  # remove item by value
my_list_jadi.append(10)
print(my_list_jadi)  # [1, 2, 4, 5, 10]


a = [1, "jadi", [1,2,3]]
print(a[2])     #[1,2,3]
print(a[2][1])  #2


result = ["sara", 15]
name, score = result
print(name)     # sara
print(score)    # 15