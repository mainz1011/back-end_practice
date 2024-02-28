# Counter()
'''
from collections import Counter
string0 = "jjjjssssvvvvvvvv"
my_counter = Counter(string0)
print(my_counter)     #results:  Counter({'v': 8, 'j': 4, 's': 4})
print(my_counter.items())    #results:  dict_items([('j', 4), ('s', 4), ('v', 8)])
print(my_counter.keys())     #results:  dict_keys(['j', 's', 'v'])
print(my_counter.values())     #results:  dict_values([4, 4, 8])
print(my_counter.most_common(2))    #results (it returns the 2 most common items consisting of a list with 2 tuples inside):  [('v', 8), ('j', 4)]
print(my_counter.most_common(2)[0])    #results (it returns the 1st item shown as a tuple):  ('v', 8)
print(my_counter.most_common(2)[0][0])   #results:  v

print(my_counter.elements())
#results:  <itertools.chain object at 0x00000227242BA350>
 #this gives us an iterable over elements repeating each as many times as it counts
print(list(my_counter.elements()))   #list() to print is nicely
#results (a list):  ['j', 'j', 'j', 'j', 's', 's', 's', 's', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'v']
'''
from collections import defaultdict

'''
# namedtuple(): an easy-to-create & lightweight object type, similar to a 'struct'.
from collections import namedtuple
Point = namedtuple('Point', 'x,y')    #here a class called 'Point' with the fields x & y (a 2D point) is created
pt = Point(7, -12)
print(pt)      #results:  Point(x=7, y=-12)
print(pt.x, pt.y)   #results:  7 -12
'''


'''
# OrderedDict(): is like a regular dict but it remembers the order that the items were inserted
from collections import OrderedDict
Ordered_Dict = OrderedDict()
Ordered_Dict['a'] = 1
Ordered_Dict['b'] = 2
Ordered_Dict['c'] = 3
Ordered_Dict['d'] = 4
print(Ordered_Dict)    #results:  OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

Ordered_Dict2 = OrderedDict()
Ordered_Dict2['d'] = 1
Ordered_Dict2['c'] = 2
Ordered_Dict2['b'] = 3
Ordered_Dict2['a'] = 4
print(Ordered_Dict2)   #results:  OrderedDict({'d': 1, 'c': 2, 'b': 3, 'a': 4})

Ordered_Dict3 = {}    #now if we use a normal dict, it will remember the order 
Ordered_Dict3['d'] = 1
Ordered_Dict3['c'] = 2
Ordered_Dict3['b'] = 3
print(Ordered_Dict3)   #results:  {'d': 1, 'c': 2, 'b': 3}
'''


'''
# defaultdict(): is similar to a usual dict container. Only difference: defaultdict() wil have a default value if the key isn't set yet
from collections import defaultdict
df = defaultdict(int)   #here 'int' is the default type
df['a'] = 1
df['b'] = 2
print(df)    #results:  defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(df['a'])    #results:  1
print(df['c'])    #results:  0  (doesn't exist. Here it gives the default value of an int which's 0 )

df2 = defaultdict(float)
df2['a'] = 1
print(df2['v'])   #results:  0.0  (doesn't exist)

df3 = defaultdict(list)
df3['a'] = 1
print(df3['s'])   #results:  []  (doesn't exist)

df4 = {}    #if we place a normal dictionary here, it'll raise a KeyError
df4['a'] = 1
df4['b'] = 2
print(df4['j'])   #shows error:  KeyError: 'j'
'''


# deque(): a double-ended queue. It efficiently adds/removes elements from both ends
from collections import deque
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.appendleft(6)
#print(dq)    #results:  deque([6, 1, 2, 3])
dq.pop()   #.pop  removes the last element
#print(dq)     #results:  deque([6, 1, 2])
dq.popleft()   #.popleft  removes the 1st element from the left side
#print(dq)    #results:  deque([1, 2])
dq.clear()
print(dq)    #results:  deque([])

dq2 = deque()
dq2.append(7)
dq2.append(9)
dq2.append(16)
#print(dq2)    #results:  deque([7, 9, 16])
#dq2.extend([8, 10, 92])
#print(dq2)   #results:  deque([7, 9, 16, 8, 10, 92])
dq2.extendleft([8, 10, 92])
#print(dq2)    #results:  deque([92, 10, 8, 7, 9, 16])
dq2.rotate(2)   #rotate each element 2 places to the right.
#print(dq2)   #results:   deque([9, 16, 92, 10, 8, 7])
dq2.rotate(-1)   #rotate each element 1 place to the left.
print(dq2)    #results:   deque([16, 92, 10, 8, 7, 9])

