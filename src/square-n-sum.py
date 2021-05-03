# Complete the square sum function so that it squares each number passed into it and
# then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.


# THIS SOLUTION IS USING 'functools'
# import functools
# def square_sum(numbers):
#     sq_numbers = [number * number for number in numbers]
#     sum_total = functools.reduce(
#         lambda acc, current: acc + current, sq_numbers)
#     print(sum_total)

# NO LIBRARY
def square_sum(numbers):
    sum_total = 0
    sq_numbers = [number * number for number in numbers]
    sum_total = sum(sq_numbers)
    return sum_total

 
print(square_sum([1, 2])) # -> 5
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
print(square_sum([-1, -2]))
print(square_sum([-1, 0, 1]))
