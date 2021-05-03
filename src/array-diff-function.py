# Your goal in this kata is to implement a difference function, which subtracts one list
# from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.
#     arrayDiff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:
#     arrayDiff([1,2,2,2,3],[2]) == [1,3]

def array_diff(array1, array2):
    result = []

    for element in array1:
        if element not in array2:
            result.append(element)
    return result


print(array_diff([1,2], [1])) #expected [2] ✅
print(array_diff([1,2,2], [1])) #expected [2,2] ✅
print(array_diff([1,2,2], [2])) #expected [1] ✅
print(array_diff([1,2,2], [])) #expected [1, 2, 2] ✅
print(array_diff([], [1,2])) #expected [] ⁉️
print(array_diff([1,2,3], [1, 2])) #expected [3] ⁉️