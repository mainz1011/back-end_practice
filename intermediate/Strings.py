'''
my_string = 'I\'m a programmer'   #or, "I'm a programmer"
print(my_string)

string2 = """Hi, 
newbie!"""
print(string2)

string3 = "Hi newbie!"
char = string3[1]
substring3 = string3[1:5]
substring4 = string3[::2]    #it takes every 2nd char
substring5 = string3[::-1]   #it reverses the string
print(char)
print(substring3)      #results:  i ne
print(substring4)      #results:  H ebe
print(substring5)      #results:  !eibwen iH

greeting = "Welcome!"
if "W" in greeting:    #case sensitive
    print('yes')
else:
    print('no')

# .strip  removes the white spaces
greeting2 = '    WELCOME BACK!          '
greeting2 = greeting2.strip()     #if just 'greeting2.strip()' without assigning, then no change to the original string (the white spaces cannot be stripped)
print(greeting2.lower())
print(greeting2.startswith('BACK!'))
print(greeting2.endswith('BACK!'))
print(greeting2.find('C'))   #case sensitive
print(greeting2.find('c'))   #results:  -1  meaning it doesn't exist
print(greeting2.replace('WELCOME','DON\'T COME'))
print(greeting2.replace('welcome','DON\'T COME'))    #it does nothing, no change to the original string

# .split()   Convert a string to a list
my_list = my_string.split()    # .split(" ") by default it looks for spaces in a string; .split(",")  here it looks for ',' in a string and then split
print(my_list)      #results:  ["I'm", 'a', 'programmer']
new_string = ''.join(my_list)
print(new_string)    #results:  I'maprogrammer
new_string2 = '   '.join(my_list)     # 3 spaces
print(new_string2)   #results:  I'm   a   programmer


# Using 'for' loop (time-consuming) or the 'join' method (better) to CONVERT a list to a string
from timeit import default_timer as timer     #compare the time running the 2 blocks of code consumed
list1 = ['a'] * 10
print(list1)     #results:  ['a', 'a', 'a', 'a', 'a', 'a']
#using 'for' loop is bad because strings are immutable,  'string1 += i'  will repetitively create a new string and then assign back to 'string1', which means it's time-consuming
start = timer()
string1 = ''
for i in list1:
    string1 += i
print(string1)   #results:  aaaaaa
stop = timer()
print(stop-start)    #if we change the multiple times to *100000, then timer shows 0.3409602999454364

#using the 'john' method is good
start = timer()
string1 = ''.join(list1)
#print(string1)
stop = timer()
print(stop-start)    #if we change the multiple times to *100000, then timer shows 0.0008712999988347292 (way more faster)
'''

# %, .format(), f-string
var1 = "Tom"
string4 = "the variable is %s" % var1     # '%s' tells the interpreter that here we have a placeholder with a string and then we fill it with 'var1'
print(string4)     #results:  the variable is Tom

var2 = 6
string5 = "the variable is %d" % var2     # '%d' a placeholder for a decimal
print(string5)     #results:  the variable is 6

var3 = 6.168886
string6 = "the variable is %f" % var3     # '%f' a placeholder for a floating point
print(string6)     #results:  the variable is 6.168886  (if '%.2f', then it will only print 2 floating digits after the decimal point, in this case the variable is shown as: 6.17)

var3 = 6.168886
string7 = "the variable is {}".format(var3)    #here we put all our elements as args
print(string7)     #results (the same with above):  the variable is 6.168886

var3 = 6.168886
string8 = "the variable is {:.2f}".format(var3)    #here insides the brackets it's ':.2f', then it will also only print 2 floating digits after the decimal point, in this case the variable is also shown as: 6.17)
print(string8)


