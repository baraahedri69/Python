#Countdown# 
def countdown(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result
countdown_list = countdown(5)
print(countdown_list) 

#Print and Return
def print_and_return(lst):
    first_value = lst[0]
    print(first_value)
    return lst[1]
result = print_and_return([1, 2])
print(result)

#First Plus Length#
def first_plus_length(lst):
    return lst[0] + len(lst)
result = first_plus_length([1, 2, 3, 4, 5])
print(result) 

#Values Greater than Second#
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_value = lst[1]
    result = [x for x in lst if x > second_value]
    print(len(result))
    return result
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3])) 

#This Length, That Value#
def length_and_value(size, value):
    return [value] * size
result1 = length_and_value(4, 7)
print(result1)
result2 = length_and_value(6, 2)
print(result2)
