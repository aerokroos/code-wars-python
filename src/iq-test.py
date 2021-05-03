# Bob is preparing to pass IQ test. The most frequent task in this test is to find
# out which one of the given numbers differs from the others. Bob observed that one
# number usually differs from the others in evenness. Help Bob — to check his answers,
# he needs a program that among the given numbers finds
# one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means
# indexes of the elements start from 1 (not 0)

# Examples
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    numbers_arr = numbers.split()
    even_position = 0
    odd_position = 0

    for i in range(0, len(numbers_arr)):
        if (int(numbers_arr[i]) % 2 == 1):
            odd_position = i + 1
        elif (int(numbers_arr[i]) % 2 == 0):
            even_position = i + 1

    if (odd_position):
        return odd_position
    elif (even_position):
        return even_position
    
print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))