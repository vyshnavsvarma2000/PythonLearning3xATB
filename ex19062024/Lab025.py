list1 = [1,2,3]
list1.extend([4,5])
print("list after extending is ", list1)



list2 = [1,2,3,4,5]
list2.append(6)
print("list after appending is ", list2)

list3 = [1,2,3,4,5,6]
list3.insert(0,10)
print("list after inserting to index 0 is",list3)

list4 = list3.copy()
print("list after copy() is ", list4)

list5 = list4.copy()
list5.sort()
print("list after sorting is ", list5)

list6 = [1,2,3,4,5,6]
list6.reverse()
print("List after reversed is ",list6)