def is_even(n):
    """
    return True if value is even
    """
    return (n % 2 == 0)
print(is_even(5))       # False
print(is_even(8))       # True

#----------------------------------------------------------------

def number_of_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    #print(count)
    return count

result = number_of_even([1,2,3,6,8,9,11,10,15])
print(result)


#----------------------------------------------------------------

def num_of_even(num):
    def is_it_even(n):
        return n % 2 == 0

    counts = 0
    for n in num:
        if is_it_even(n):
            counts += 1
    return counts
res =num_of_even([1,2,3,4,5,6,7,8,15,19,14])
print(res)

#-----------------------------------------------------------------

def any_even_in_list(nums):
    """
    return True if ANY of numbers is even
    """
    for n in nums:
        if is_even(n):
            return True
    return False
my_numbers = [1,2,3,4,5]
print(any_even_in_list(my_numbers))

#----------------------------------------------------------------

def largest(nums):
    """
    find largest number in list
    """
    largest_number = nums[0]
    for n in nums:
        if largest_number < n :
            largest_number = n
    return largest_number

my_nums = [1, 5, 8, 3, 9, 11, 7]
largest_number = largest(my_nums)
print(largest_number)


#---------------------------------------------------------------

def is_evens(n):
    return n % 2 == 0

def get_odd(numbers):
    result = []
    for n in numbers:
        if not is_evens(n):
            result.append(n)
    return result

my_list = [1, 2, 4, 7, 5, 8, 9, 6]
my_odds = get_odd(my_list)
print(my_odds)
print(len(my_odds))