'''
from itertools import product
a = [2, 4]
b = [6, 8]
c = [16]
prod = product(a, b)
prod2 = product(b, c)
prod3 = product(b, c, repeat=2)
#print(prod)   #results:  <itertools.product object at 0x0000018829E23A40>
print(list(prod))    #results:  [(2, 6), (2, 8), (4, 6), (4, 8)]
print(list(prod2))   #results:  [(6, 16), (8, 16)]
print(list(prod3))   #results:  [(6, 16, 6, 16), (6, 16, 8, 16), (8, 16, 6, 16), (8, 16, 8, 16)]
'''


'''
from itertools import permutations
a = [6, 8, 17]
perm = permutations(a)
print(list(perm))    #results:  [(6, 8, 17), (6, 17, 8), (8, 6, 17), (8, 17, 6), (17, 6, 8), (17, 8, 6)]
perm2 = permutations(a, 2)
print(list(perm2))   #results:  [(6, 8), (6, 17), (8, 6), (8, 17), (17, 6), (17, 8)]
'''


'''
from itertools import combinations, combinations_with_replacement
a = [6, 8, 17, 4]
comb = combinations(a, 2)
print(list(comb))     #results:  [(6, 8), (6, 17), (6, 4), (8, 17), (8, 4), (17, 4)]
comb_wr = combinations_with_replacement(a, 2)    #this makes repetition of the same arg
print(list(comb_wr))  #results:  [(6, 6), (6, 8), (6, 17), (6, 4), (8, 8), (8, 17), (8, 4), (17, 17), (17, 4), (4, 4)]
'''
'''
In mathematics, permutation & combination are two different ways of grouping elements of a set into subsets. 
In a permutation, the elements of the subset are listed in a specific order. 
In a combination, the elements of the subset can be listed in any order. 
'''


'''
from itertools import accumulate
import operator    #multiply
a = [6, 8, 17, 4, 1]
acc = accumulate(a)
acc2 = accumulate(a, func=operator.mul)
acc3 = accumulate(a, func=max)
print(list(acc))   #results:  [6, 14, 31, 35, 36]
print(list(acc2))  #results:  [6, 48, 816, 3264, 3264]
print(list(acc3))  #results:  [6, 8, 17, 17, 17]
'''


'''groupby() func & lambda func
# groupby() func makes an iterator that returns groups & keys from an iterable.  
 # lambda func: a small 1 line anonymous func that can have an input and will do some expression and then will return an output
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [6, 8, 17, 4, 1]
#group_obj = groupby(a, key=smaller_than_3)
group_obj = groupby(a, key=lambda x: x<3)
#print(group_obj)    #results:  <itertools.groupby object at 0x000001BC8E46D660>
for key, value in group_obj:
    #print(key, value)    #results:  False <itertools._grouper object at 0x00000162DD7FCF70>
                                    #True <itertools._grouper object at 0x00000162DD7FD060>
    print(key, list(value))   #results: False [6, 8, 17, 4]
                              #True [1]
'''


'''
from itertools import groupby

persons = [{'name': 'Hannah', 'age': 18}, {'name': 'Alice', 'age': 18},
           {'name': 'Xin', 'age': 36}, {'name': 'Aurora', 'age': 33}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))    #results:  18 [{'name': 'Hannah', 'age': 18}, {'name': 'Alice', 'age': 18}]
                                         #36 [{'name': 'Xin', 'age': 36}]
                                         #33 [{'name': 'Aurora', 'age': 33}]
'''


# 'count', 'cycle', 'repeat' functions
from itertools import count, cycle, repeat
'''
for i in count(6):
    print(i)
    if i == 18:
        break
'''
'''
a = [6, 8, 17, 4, 1]
for i in cycle(a):
    print(i)
    if i == 17:
        break
'''
a = [6, 8, 17, 4, 1]
for i in repeat(8, 7):
    print(i)   #8 is repeated for 7 times

