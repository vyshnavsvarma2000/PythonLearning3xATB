lst = [1,2,3,4,5]

#Map()

def double_item(num):
    return num * 2

double_list = list(map(double_item, lst))
print(double_list)