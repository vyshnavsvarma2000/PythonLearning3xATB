my_list = [1,2,3,4,5]

def double(num):
    return num*2

#Map() function
#Takes each item from the list
#execute the function on it
#Return same number of elements (list)

double_list = list(map(double, my_list))
print(double_list)


#using lambda function
lam_list = [10,20,30,40]
result = list(map(lambda num:num*2, lam_list))
print("Lambda function result is ", result)

#tuple modification
tup = (1,2,3,4,5)
lst = list(tup)
lst[0] = 5
tup = tuple(lst)
print(tup)