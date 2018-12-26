'''Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending 
to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.'''
#Example output: sums([1, 2, 2, 6, 99, 99, 7]) → 5

def func():
    L = [1, 2, 2, 6, 99, 99, 7, 1]
    my_sum = 0
    no_sum = False

    for i in range(0, len(L)):
        if L[i] == 6:
            no_sum = True
            my_sum = my_sum + 0

        elif no_sum == True and L[i] == 7:
            no_sum = True
            my_sum = my_sum + 0

        if no_sum == False:
            my_sum = my_sum + L[i]

    return my_sum


print(func())
