from cssorting_array import Sorting_array

SIZE_OF_ARRAY = 100
NEGATIVE_LOW = -10000
SMALLEST_NUMBER_TO_BE_SORTED = 0
LARGEST_NUMBER_TO_BE_SORTED = 10000

test_array = Sorting_array(SIZE_OF_ARRAY)

test_array.fill_negative(NEGATIVE_LOW, SMALLEST_NUMBER_TO_BE_SORTED)
test_array.quick_sort()
print(test_array.test_return())

test_array.fill_positive_and_negative(NEGATIVE_LOW, LARGEST_NUMBER_TO_BE_SORTED)
test_array.quick_sort()
print(test_array.test_return())
