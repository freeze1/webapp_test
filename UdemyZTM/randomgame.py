# from array import array
# import datetime
# from collections import Counter, defaultdict, OrderedDict
# import pyjokes
# from random import randint
# import sys

# from random import shuffle
# import sys
# from utility import multiply, divide
# from shopping.more_shopping import shopping_cart
#
# # print(utility)
# if __name__ == '__main__':
#     print(shopping_cart.buy('apple'))
#     print(divide(5, 2))
#     print(multiply(5, 2))
#     print(max([1, 2, 3]))
#
#     print(__name__)
#     print('please run this')

# my_list = [1, 2, 3, 4, 5]
# shuffle(my_list)
# print(my_list)
# print(sys)
# sys.argv

# generate a number 1-10
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# input from user?

# check that input is a number 1-10
# while True:
#     try:
#         print(answer)
#         guess = int(input('guess a number 1-10 '))
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius')
#                 break
#         else:
#             print('hey bozo, I said 1-10')
#     except ValueError:
#         print('please enter a number ')
#         continue

# joke = pyjokes.get_joke('en','neutral')
# print(joke)

# li = [1,2,3,4,5,6,7,7,]
# sentence = 'blah blah blah thinking about python'
# print(Counter(li))
# print(Counter(sentence))
#
# dictionary = defaultdict(lambda:'does not exist',{'a':1,'b':2})
# print(dictionary['c'])

# d = OrderedDict()
# d = {'c':100}
# d['a'] = 1
# d['b'] = 2
#
# # d2 = OrderedDict()
# d2 = {'c':100}
# d2['b'] = 2
# d2['a'] = 1
#
# print(d2 ==d)

# print(datetime.date.today())

# arr = array('i', [1,2,3])
# print(arr[0])
# debugging
# linting
# ide/editor/pep8
# read errors
# pdb
# 'name' +4
import pdb


def add(num1, num2):
    pdb.set_trace()
    t = 4+5
    return num1+num2

add(4, 5)



