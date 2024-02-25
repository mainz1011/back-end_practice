odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

#.union
u = odds.union(primes)
print(u)    #it prints:  {1, 2, 3, 5, 7, 9}

#.intersection: find common elements
i1 = odds.intersection(evens)
print(i1)    #it prints an empty set:  set()

i2 = odds.intersection(primes)
print(i2)    #it prints:  {3, 5, 7}

i3 = evens.intersection(primes)
print(i3)

#.difference: find unique elements of each other
diff1 = odds.difference(primes)
print(diff1)    #it prints:  {1, 9}

diff2 = primes.difference(odds)
print(diff2)    #it prints:  {2}

#.symmetric_difference: find all different elements
sym_diff = primes.symmetric_difference(odds)
print(sym_diff)   #it prints:  {1, 2, 9}

#.update, .intersection_update, .difference_update, .symmetric_difference_update: directly update a set
'''
odds.update(primes)
print(odds)     #'odds' set is updated. It also prints as long as the original 'odds' set doesn't change:  {1, 2, 3, 5, 7, 9}
'''
'''
odds.intersection_update(primes)
print(odds)     #'odds' set is updated. It also prints as long as the original 'odds' set doesn't change:  {3, 5, 7}
'''
'''
odds.difference_update(primes)
print(odds)     #'odds' set is updated. It also prints as long as the original 'odds' set doesn't change:  {1, 9}
'''
odds.symmetric_difference_update(primes)
print(odds)     #'odds' set is updated. It also prints as long as the original 'odds' set doesn't change:  {1, 2, 9}









