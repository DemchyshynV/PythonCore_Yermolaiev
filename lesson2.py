l = [1, 2, 3, 4, 2, 3]
s = set(l)
# list1 = list(s)
# print(list1)
# s1 = set()
# s1.add(2)
# s1.add(2)
# s1.add(3)
# print(s1)
# print(type(s1))
set1 = {1, 2, 3, 4, 5}
set2 = {8, 9, 2, 10, 5}

# print(set1.issuperset(set2))
# print(set2.issubset(set1))
# print(set1.isdisjoint(set2))
# union = set1.union(set2)
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(union)
# set1.remove(22)
# set1.discard(22)
# print(set1)
# l = []
# while set1:
#     l.append(set1.pop())
#
# print(l)

########################################################################################
# string = "name = \"Vasia\""
# print(string)
#
# name = 'Max'
# age = 18

# string = 'hello my name is ' + name + ' my age is ' + str(age)
# string = 'hello my name is %s my age is %d' % (name, age)
# string = 'hello my name is {} my age is {}'.format(name, age)
# string = 'hello my name is {name} my age is {age}'.format(age=age, name=name)
# string = f'hello my name is {name} my age is {age}'
#
# print(string)

# string = 'hello my naisme is max my age is 18'

# print(string.index('is',12,18))
# print(string.find('1'))
# print(string.count('Z'))
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.isupper())
# print(string.islower())
# print('hello world'.title())
# print('Hello World'.swapcase())
# print('1d'.isdigit())
# st = '1d'
# if st.isdigit():
#     i = int(st)
# print('hello world'.isalpha())
# print('hello1world'.isalnum())
# print('hello'.startswith('hel'))
# print('hello'.endswith('hel'))
# print('hello'.('hel'))
# strip = 'aaa   jdfj    aaa'.rstrip('a')
# print([strip])
# split = 'hello world'.split()
# split = 'hello-world'.split('-')

# partition = 'hello is world is'.partition('is')
# print(partition)
# l = ['hello', 'world']
# join = '-'.join(l)
# print(join)

# print('hello world'.replace('l', 'w'))

# string = 'hello world'
# print(string[::2])
##################################################################################
# print(min([2, 3, 4, 5, 6]))
# print(max([2, 3, 4, 5, 6]))
# print(sorted([2, 5, 3, 6]))
# f = pow(2, 25)
# print(f)

# a, b,_,c,*_ = [1, 2,5,5,6]
# print(a)
# print(b)
# print(c)

# a=5
# b = 6
# a,b = (b,a)

# print(a)
# print(b)
###############################################################
# list Comprehension

# range_ = [i for i in range(10) if i >5]
# print(range_)
# world = ['hello', '3', 'world', '2']
# list = [item for item in world if item.isalpha()]
# print(list)
# arr.filter(value=>value>5)

# range_ = [i ** 2 for i in range(10) if i % 2 == 0]
# print(range_)
# l1 = [[1, 2, 3, 4], [5, 6, 7, 8,1]]
#
# item_ = [i for item in l1 for i in item]
#
# arr = []
# for i in l1:
#     for j in i:
#         arr.append(j)
#
# print(arr)

# def func(a, b, c=6, *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
#
# func(3, 5, 99, name='Max', age=13)
#
# def greeting():
#     print('hello')

# print('************************************')
# greeting()
# print('************************************')

# def decor(func):
#     print('************************************')
#     func()
#     print('************************************')


# # decor(greeting)
# def decor(func):
#     def wrap(*args,**kwargs):
#         print('************************************')
#         func(*args, **kwargs)
#         print('************************************')
#
#     return wrap
#
# @decor
# def greeting():
#     print('hello')
#
# greeting()
#
# @decor
# def summ(a,b):
#     print(a+b)
#
# summ(5,7)

# dic = {
#     'name': 'max',
#     'age': 13
# }
#
#
# def user(name, age):
#     print(name)
#     print(age)
#
#
# user(**dic)
#
# def summ(a, b):
#     return a + b
#
#
# summ2 = lambda a, b: a + b
#
# print(summ2(5, 7))
l = [1, 2, 3, 4, 6]

i = map(lambda x: x + 1, l)
list1 = list(i)
print(list1)

l_ = [i + 1 for i in l]
print(l_)
