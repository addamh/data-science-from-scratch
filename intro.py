from __future__ import division

__author__ = 'addam'

def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

print x

y = apply_to_one(lambda x: x + 4)

print y

def another_double(x): return 2 * x

def my_print(message="my default message"):
    print message

my_print("hello")
my_print()

def subtract(a=0, b=0):
    return a - b

print subtract(10, 5)
print subtract(0, 5)
print subtract(b=5)

single_quoted_string = 'string'
double_quoted_string = "string"
tab_string = "\t"
print len(tab_string)

multi_line_string = """This is the first line.
and this is the second line.
and this is the third line."""

try:
    print 0 / 0
except ZeroDivisionError:
    print "cannot divide by zero dumbass"

print "----"

integer_list = [1, 2, 3]
heterogenous_list = ["string", 0.1, True, 4]
list_of_lists = [integer_list, heterogenous_list]

list_length = len(integer_list)
list_sum = sum(integer_list)

print list_length
print list_sum

print "----"

x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

print 1 in [1, 2, 3]
print 0 in [1, 2, 3]

x = [1, 2, 3]
x.extend([4, 5, 6])

x = [1, 2, 3]
y = x + [4, 5, 6]

x = [1, 2, 3]
x.append(0)

y = x[-1]
z = len(x)



