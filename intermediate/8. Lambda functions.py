# lambda func: a small 1 line anonymous func that's defined without a name. it's typically used as simple func that used only once.
   #It can also be used as an arg to high-order functions, meaning functions that take in other functions as arg, e.g., being used along with built-in functions (filter(), map(), sorted()) and func like reduce().
 # lambda args: expression    (this will create a function with some args, and then it evaluates the expresion and returns the result)
''' compare below 2 blocks of code doing the same adding, clearly using lambda func is more efficient
def add8_func(x):
    return x + 8
print(add8_func(6))
'''
'''
add8 = lambda x: x + 8
print(add8(6))    #results:  14
'''

'''
mult = lambda x,y: x*y
print(mult(6,8))    #results:  48
'''


# sorted()
#points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
'''
points2D_sorted = sorted(points2D)
print(points2D_sorted)    #results:  [(1, 2), (5, -1), (10, 4), (15, 1)]
'''
'''
points2D_sorted = sorted(points2D, key=lambda x: x[1])    #here we use lambda func to sort according to the 2nd element in each tuple
print(points2D_sorted)    #results:  [(5, -1), (15, 1), (1, 2), (10, 4)]
'''


# map(func, seq): transforms each element with a func
'''
a = [8, 16, 17, 4, 22, 9]
b = map(lambda x: x*2, a)
#print(b)    #results (a map object is printed):  <map object at 0x000001F0E1C85480>
print(list(b))    #results:  [16, 32, 34, 8, 44, 18]

#here the list comprehension syntax can more efficiently do the same as the map() func
c = [x*2 for x in a]
print(c)    #results:  [16, 32, 34, 8, 44, 18]
'''


'''
# filter(func, seq)
a = [8, 16, 17, 4, 22, 9]
b = filter(lambda x: x%2==0, a)   #get the even numbers
print(list(b))    #results:  [8, 16, 4, 22]
#here the list comprehension syntax can achieve the same as well
c = [x for x in a if x%2==0]
print(c)    #results:  [8, 16, 4, 22]
'''


# reduce(func, seq): it repeatedly applies the func to the elements, and then returns a single value.
from functools import reduce
a = [8, 16, 17, 4, 22, 9]

prod_a = reduce(lambda x,y: x*y, a)
print(prod_a)     #results:  1723392

