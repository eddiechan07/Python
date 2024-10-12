# Countdown
def countdown(start_number):
    result = []
    for int in range(start_number, 0, -1):
        result.append(int)
    return result
print(countdown(5))

#Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
list = [1,2]
print(print_and_return(list))

# First Plus Length
list = [1,2,3,4,5]
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length(list))

#Values Greater than Second
def values_greater_than_second(list1):
    list2 = []
    sum = 0
    if len(list1)<2:
        return False
    for int in list1:
        if int >list1[1]:
            sum +=1
            list2.append(int)
    print(sum)
    return list2
listA = [5,2,3,2,1,4]
listB = [3]
print(values_greater_than_second(listA))
print(values_greater_than_second(listB))

#This Length, That Value
def length_and_value(a,b):
    list =[]
    for int in range(a):
        list.append(b)
    return list

print (length_and_value(4,7))
print (length_and_value(6,2))