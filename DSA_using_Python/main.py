from datetime import datetime

import pandas as pd
import numpy as np

def decorator_fun(arg1,arg2):
    def thefunc(my_func):
        def temp():
            print(f"this is a decorator test print statement{arg1},{arg2}")
            my_func()
            print("after executing the original imp function",arg1,arg2)
        return temp
    return thefunc


@decorator_fun("hey","there")
def func():
    print("hey there")
    print(datetime.now())

func()


def generator_func():
    for i in range(5):
        yield i



store_generator = generator_func()

# for i in store_generator:
#     print(i)

print(next(store_generator))

array = [1,2,43,4,4]

my_list = [x*x if x%2==0 else x for x in array]
print(my_list)

# for i in gen:
#     print(i)

add = lambda x:x+1

print(add(10))

freq_map = [{"hey":"there"},{"hey":"kdsakfsa"},{"hey":"w4234"}]

test_map = {"hey":2324,"hey":2432423}

print(dict(sorted(test_map.items(),reverse=True)))

new_array = sorted(freq_map,key=lambda x:x["hey"],reverse=True)

print(new_array)

series_ = pd.Series(array)
print(series_)


temp_array = [1,2,3,4,4,5,3]

arr = [x if x%2!=0 else x*x for x in temp_array]
print(arr)



arr = sorted(test_map.values(),reverse=True)
print(arr)



def _closure(n):
    def temp():
        print(n)
    return temp


my_clsre  = _closure(15)
my_clsre()


np_array = np.array([1,2,3,5])
print(np_array)


np_array = np.array([1,2,3,45])
np_array2 = np.array([1231,3243,33,34])

print(np_array+np_array2)

tup =(1,2,3,3)



tup+=(4,)
print(tup)

arr = list(tup)
arr.append(15)
print(tuple(arr))


my_new_tuple = (1,2,2131,13213)

my_new_tuple = list(my_new_tuple)
my_new_tuple.remove(2)

my_new_tuple=tuple(my_new_tuple)

print(my_new_tuple)



my_list = [12,2,2,2,24,21313,13131]



my_list.pop()
print(my_list)


def gen_fun(func):
    def temp_func():
        print("hey this is a decorator function")
        func()
        print("hey after calling decorator function")
    return temp_func



@gen_fun
def original_func():
    print("testing here")


original_func()
