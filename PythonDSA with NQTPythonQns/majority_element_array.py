
def majority(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1
    return i



print(majority([1,2,3,4,2,5,2,1,1,1]))



