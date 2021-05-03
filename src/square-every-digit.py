# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    if num == 0:
        return num
        
    sq_numbers = []
    str_num = str(num)
    for num in str_num:
        sq_numbers.append(str(pow(int(num), 2)))
    return (int("".join(sq_numbers)))

print(square_digits(9119))
print(square_digits(0))