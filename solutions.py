# leap year problem
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
                return leap
            return leap
        leap = True
    return leap

year = int(input())

# printing in a line
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")
 
# Regular Expression validity checker
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    length = input()
    exp_str = []
    for i in range(int(length)):
        exp_str.append(input())

    validity_value = []
    for expression in exp_str:
        try:
            re.compile(expression)
            is_valid = True
        except re.error:
            is_valid = False
        validity_value.append(is_valid)
        
    for elem in validity_value:
        print(elem)
 
 # Exception
 # Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    length = int(input())
    operands = []
    for i in range(length):
        operands.append(input()) # change this to raw_input for Python 2
    
    for i in operands:
        a = i.split()[0]
        b = i.split()[1]
        try:
            print(int(a)/int(b))
        except (ZeroDivisionError, ValueError) as e:
            msg = e
            if e == 'division by zero':
                msg = 'integer division or modulo by zero'
            print("Error Code: {}".format(msg))

# Set subset checker
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    test_cases = int(input())
    is_subset_value = []
    for i in range(test_cases):
        set1_length = int(input())
        set1_elements = input()
        set1 = set(set1_elements.split())
        set2_length = int(input())
        set2_elements = input()
        set2 = set(set2_elements.split())
        is_subset = set1.issubset(set2)
        is_subset_value.append(is_subset)
    for el in is_subset_value:
        print(el)
        
# Cuboid
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    result.append([i,j,k])        
    print(result)


# scoresheet runner-up score
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(list(set(arr)))[-2])
    
# Nested lists
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        names.append(name)
        scores.append(score)
    
    second_last_score = sorted(list(set(scores)))[1]
    second_last_students = []
    for name, score in zip(names,scores):
        if score == second_last_score:
            second_last_students.append(name)
    for name in sorted(second_last_students):
        print(name)


# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_mark = student_marks[query_name]
    total = 0.0
    for mark in student_mark:
        total += mark
    print(format(total/len(student_mark), ".2f"))
    
# polynomials
import numpy

coefficients = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(coefficients, x))

# Linear Algebra
import numpy

n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(a))


# Calendar Module
import calendar as ca
d,m,y = ([int(i) for i in input().split()])
a = ca.weekday(y,d,m)
n = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(n[a])


# Time delta
#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((first-second).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Collections counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    number_of_shoes = int(input())
    shoe_size = list(map(int, input().split()))
        
    number_of_orders = int(input())
    orders = []
    for _ in range(number_of_orders):
        orders.append(list(map(int, input().split())))
    
    shoes_qty = Counter(shoe_size)
    total_price = 0
    
    for order in orders:
        size = order[0]
        price = order[1]
        size_avail = shoes_qty[size]
        if size_avail > 0:
            total_price += price
            shoes_qty[size] -= 1
            
    print(total_price)
            
# DefaultDict

from collections import defaultdict

if __name__ == '__main__':
    n, m = list(map(int,input().split()))
    
    a = defaultdict()
    b = defaultdict()
    for i in range(1, n+1):
        a[i] = input()
    
    for j in range(1, m+1):
        b[j] = input()
    
    result = []
    for _,b_element in b.items():
        not_appeared = True
        for index, a_element in a.items():
            if b_element == a_element:
                print(index, end=" ")
                not_appeared = False
        if not_appeared:
            print(-1, end=" ")
                
        print('')
  
# Collection namedtuples
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    cols = input()
    Record = namedtuple('record', cols)
    records = []
    
    for _ in range(n):
        current_records = input().split()
        rec = Record(*current_records)
        records.append(rec)
    
    total = 0
    for record in records:
        total += int(record.MARKS)
    average = total/n
    print(average)
    
# Collections orderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    
    result = OrderedDict()
    for _ in range(n):
        line = input().split()
        price = int(line[-1])
        item_name = line[:len(line)-1]
        item_name = ' '.join(str(e) for e in item_name)
        result[item_name] = result[item_name] + price if item_name in result else price
    for key, val in result.items():
        print(key, val)
   
 # Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    
    words = []

    result = OrderedDict()
    for _ in range(n):
        word = input()
        result[word] = result[word] + 1 if word in result else 1
    print(len(result))
    for key, val in result.items():
        print(val, end=" ")
  
# deque
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    for _ in range(n):
        op_val = input().split()
        length = len(op_val)
        if length > 1:
            getattr(d, op_val[0])(op_val[1])
        else:
            getattr(d, op_val[0])()
    for val in d:
        print(val, end=" ")
        
        
        
        
 #########
 for _ in range(t):
        cube_horizontal = deque()
        cube_vertical = deque()
        n = int(input())
        elements = input().split()
        cube_horizontal.extend(elements)
        result = "Yes"
        while(len(cube_horizontal) > 0):
            first = cube_horizontal[0]
            last = cube_horizontal[-1]
            target_element = first if first > last else last
            if len(cube_vertical) == 0:
                if target_element == cube_horizontal[0]:
                    cube_horizontal.popleft() 
                else:
                    cube_horizontal.pop()
                cube_vertical.append(target_element)  
            else:       
                if target_element <= cube_vertical[-1]:
                    if target_element == cube_horizontal[0]:
                        cube_horizontal.popleft() 
                    else:
                        cube_horizontal.pop()
                    cube_vertical.append(target_element)
                    # print(cube_horizontal, cube_vertical)
                else:
                    result = "No"
                    # print(cube_horizontal, cube_vertical)
                    break
        print(result)  
    
# List operations    
if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    for _ in range(N):
        command  = input().split()
        meth = command[0]
        args = list(map(int, command[1:len(command)]))
         
        if len(args) > 0:
            getattr(my_list, meth)(*args)   
        elif meth == 'print':
            print(my_list)
        elif meth == 'sort':
            my_list = sorted(my_list)
        elif meth == 'reverse':
            my_list.reverse()
        elif meth == 'pop':
            my_list.pop()
            
######################## 5 STARS ACHIEVED ##########################
# String validators
if __name__ == '__main__':
    s = input()
    if any(char.isalnum() for char in s):
        print(True)
    else:
        print(False)
        
    if any(char.isalpha() for char in s):
        print(True)
    else:
        print(False)
        
    if any(char.isdigit() for char in s):
        print(True)
    else:
        print(False)
        
    if any(char.islower() for char in s):
        print(True)
    else:
        print(False)
        
    if any(char.isupper() for char in s):
        print(True)
    else:
         print(False)
         
         
         
         
###################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(100000)

def charcount(string, result, index = 0):
    count = 0
    i = index
    prev = string[index]
    while(prev == string[i]):
        count += 1
        if(i == len(string)-1):
            break
        i += 1
    result.append((count, int(string[index])))
    if i != len(string)-1:
        charcount(string, result, i)

if __name__ == "__main__":
    arg = input()
    result = []
    charcount(arg, result)
    if len(arg) > 1:
        if arg[-1] != arg[-2]:
            result.append((1, int(arg[-1])))
    print(*result)
   