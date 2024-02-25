'''
setA = {1, 2, 3, 4, 5, 8, 12}
setB = {1, 2, 3}
setC = {7, 16}

print(setA.issubset(setB))     #False
print(setB.issubset(setA))     #True

print(setB.issuperset(setA))   #False

#True if no same elements
print(setB.isdisjoint(setA))   #False
print(setB.isdisjoint(setC))   #True
'''

#NOTE:
'''
setA = {1, 2, 3, 4, 5, 8, 12}
setB = setA   #with this simple assignment, both point to the same set, so the results are the same. Be careful here as only the reference is copied 

setB.add(10)
print(setB)     #prints:  {1, 2, 3, 4, 5, 8, 10, 12}
print(setA)     #prints:  {1, 2, 3, 4, 5, 8, 10, 12}
'''

#to make a real copy, use  .copy  or  set()
setA = {1, 2, 3, 4, 5, 8, 12}

#setB = setA.copy()
setB = set(setA)
setB.add(10)
print(setB)    #setB: {1, 2, 3, 4, 5, 8, 10, 12}
print(setA)    #setA isn't changed

# frozenset()  is immutable, .add  .remove  would all show error
a = frozenset([1, 2, 3, 4])
#a.add(6)     #AttributeError: 'frozenset' object has no attribute 'add'
print(a)      #results:  frozenset({1, 2, 3, 4})





