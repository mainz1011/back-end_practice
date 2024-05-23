# SyntaxError
#a = 6 print(a)    #SyntaxError: invalid syntax


#exceptions
#a = 6 + '18'    #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#import somemodule    #ModuleNotFoundError: No module named 'somemodule'

'''
a = 5
b = c     NameError: name 'c' is not defined
'''

#f = open('somefile.txt')    #FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

#ValueError (it happens when the func / operation receives an arg that has the right type but an inappropriate value)
a = [8, 16, 17, 4, 22, 9]
#a.remove(17)     #results:  [8, 16, 4, 22, 9]
#a.remove(11)     #ValueError: list.remove(x): x not in list
#a[6]     #IndexError: list index out of range
print(a)

'''
my_dict = {'name': 'Max'}
my_dict['age']     #KeyError: 'age'
'''



# Raise an exception
'''
x = -6
if x < 0:
    raise Exception('x should be positive')     #Exception: x should be positive
                                                 #if x >= 0 then no 'Exception' would be raised
'''
#in this case, the 'assert' statement does the same job
'''
x = -6
#assert (x>=0)     #results:  AssertionError
assert (x>=0), 'x is not poitive'     #results:  AssertionError: x is not poitive
'''

#the exceptions can be caught with a 'try    except' block
#a = 5 / 0    #results:  ZeroDivisionError: division by zero

'''
try:
    a = 5 / 0    #SyntaxError: expected 'except' or 'finally' block
'''

'''
try:
    a = 5 / 0
except:
    print('an error occurred')    #results:  an error occurred
'''

'''
try:
    a = 5 / 0
except Exception as e:
    print(e)     #results:  division by zero
'''

'''
try:
    a = 5 / 0
    b = a + '6'
except ZeroDivisionError as e:
    print(e)    #results:  division by zero
except TypeError as e:
    print(e)
'''

'''
try:
    a = 5 / 1
    b = a + '6'
except ZeroDivisionError as e:
    print(e)     #TypeError: unsupported operand type(s) for +: 'float' and 'str'
'''

'''
try:
    a = 5 / 1
    b = a + '6'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)    #results:  unsupported operand type(s) for +: 'float' and 'str'
'''

'''
try:
    a = 5 / 1
    b = a + 6
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')     #results:  everything is fine
'''

'''
try:
    a = 5 / 0
    b = a + 6
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:    #'finally' is used to make some cleanup operations
    print('cleaning up...')
#results:  division by zero
           cleaning up...
'''



# Define our own exception: we define our own error classes by sub-classing from their base 'Exception' class
 #below is a valid, defined error
'''
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')


#test_value(200)    #ValueTooHighError: value is too high
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)     #results:  value is too high
'''


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 7:
        raise ValueTooSmallError('value is too small', x)


#test_value(200)    #ValueTooHighError: value is too high
try:
    test_value(4)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)     #results:  value is too small 4


