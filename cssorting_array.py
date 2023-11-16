# cssorting_array.py
# Slade Leicht
# 2023.02.04
# File contains the class Sorting_array

# Class Sorting_array can fill itself with random numbers, with one random repeated number,
# with random increasing numbers, and with random decreasing numbers. It can also sort
# itself from smallest to largest and print.


from csarray import Array

import random


class Sorting_array(Array):
	""" Implement an array with the ability to sort itself.

	The class Sorting_array will inherit from class Array, will be able to fill itself
	with random, the same, increasing, and decreasing numbers, and will be able to
	sort its contents from smallest to largest.
	"""

	def __init__(self, size, default_value=None):
		""" Create a Sorting array object. """

		super().__init__(size, default_value)

	def fill_negative(self, NEGATIVE_LOW, SMALLEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated negative numbers. """

		for i in range(self.size):
			self.data[i] = random.randint(NEGATIVE_LOW, SMALLEST_POSSIBLE_NUMBER)

	def fill_positive_and_negative(self, NEGATIVE_LOW, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly genereated positive and negative numbers. """

		for i in range(self.size):
			self.data[i] = random.randint(NEGATIVE_LOW, LARGEST_POSSIBLE_NUMBER)

	def fill_random(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated numbers. """

		# Used for testing how the sorts handle random numbers
		for i in range(self.size):
			self.data[i] = random.randint(SMALLEST_POSSIBLE_NUMBER,
						      LARGEST_POSSIBLE_NUMBER)

	def fill_same(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill each spot of the array with the same randomly generated number. """

		# Used for testing how the sorts handle repeated numbers
		NUMBER_THAT_WILL_FILL_THE_ARRAY = random.randint(SMALLEST_POSSIBLE_NUMBER,
								 LARGEST_POSSIBLE_NUMBER)

		for i in range(self.size):
			self.data[i] = NUMBER_THAT_WILL_FILL_THE_ARRAY

	def fill_increasing(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated increasing numbers. """

		# Used for testing how the sorts handle already sorted arrays.
		random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER,
						  LARGEST_POSSIBLE_NUMBER)

		for i in range(self.size):
			self.data[i] = random_integer

			# Generate a random interval to increase each number by
			interval = random.randint(SMALLEST_POSSIBLE_NUMBER,
						  LARGEST_POSSIBLE_NUMBER)
			random_integer += interval

	def fill_decreasing(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated decreasing numbers. """

		# Used for testing how the sorts handle a decreasing array.
		random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER)

		for i in range(self.size):
			self.data[i] = random_integer

			interval = random.randint(SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER)
			random_integer -= interval

	def fill_even(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated even numbers. """

		# Used for testing how the sorts handle an array with random even integers.
		for i in range(self.size):

			random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER,
						        LARGEST_POSSIBLE_NUMBER)

			while random_integer % 2 != 0:
				random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER,
							        LARGEST_POSSIBLE_NUMBER)

			self.data[i] = random_integer

	def fill_odd(self, SMALLEST_POSSIBLE_NUMBER, LARGEST_POSSIBLE_NUMBER):
		""" Fill the array with randomly generated odd numbers. """

		# Used for testing how the sorts handle an array with random odd integers.
		for i in range(self.size):

                        random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER,
							LARGEST_POSSIBLE_NUMBER)

                        while random_integer % 2 == 0:
                                random_integer = random.randint(SMALLEST_POSSIBLE_NUMBER,
								LARGEST_POSSIBLE_NUMBER)

                        self.data[i] = random_integer

	def insertion_sort(self, h=1):
		""" Sort integers in the array from smallest to largest. """

		# Sort arrays by sorting boxes h boxes apart from one another, repeatedly passing
		# through the array until sorted.
		for i in range(h, self.size):

			key = self.data[i]
			j = i

			while j > (h - 1) and self.data[j - h] > key:
				self.data[j] = self.data[j - h]
				j = j - h

			# Move the value in box i, don't lose it.
			self.data[j] = key

	def shell_sort(self):
		""" Sort numbers in an array using the shell sort method from smallest to largest.

		Uses the same compare-insert method as insertion sort except the increment, h, between
		boxes is initially greater than one and decreases.
		"""

		# Define the increment between compared boxes. This doesn't generate the fastest
		# possible increments, but it's pretty fast.
		h = 1
		while h < self.size:
			h = 3 * h + 1

		while h > 1:

			# h should be able to compare multiple numbers in the array.
			h = (h - 1) // 3
			self.insertion_sort(h)

	def make_a_heap(self, k, limit):
		""" Convert an array into a heap. """

		# limit is the number of remaining elements in the array.
		if limit > 1:

			key = self.data[k]

			is_heap = False

			# While the node has children and isn't a heap
			while k <= (limit - 2)//2 and not is_heap:

				# j initially is the left child. If there is a right child greater
				# than the left, j is the right child.
				j = 2 * k + 1

				if j + 1 < limit:
					if self.data[j] < self.data[j + 1]:
						j = j + 1

				# Checks if the parent is greater than the larger child. If not,
				# move the larger child up.
				if key >= self.data[j]:
					is_heap = True

				else:
					self.data[k] = self.data[j]
					k = j

			self.data[k] = key

	def heap_sort(self):
		""" Sort integers in an array by repeatedly converting the array into a heap. """

		n = self.size

		# (n - 2) // 2 refers to the last box with a child.
		# -1 includes box 0 in the sorting.
		# -1 sorts from back to front, moving the largest number to the root node.
		for i in range((n - 2) // 2, -1, -1):
			self.make_a_heap(i, n)

		# Excludes the largest number after moving it to the last node
		for m in range (n - 1, 0, -1):

			temp = self.data[m]
			self.data[m] = self.data[0]
			self.data[0] = temp

			self.make_a_heap(0, m)

	def partition(self, left, right):
		""" Draw a partition line and return the number to the right of it. """

		pivot = self.data[left]
		i = left
		j = right

		while i <= j:

			# Move i to the right until it finds a number on the wrong side of the
			# partition.
			while self.data[i] < pivot:
				i += 1

			# Move j to the left until it finds a number on the wrong side of the
			# partition.
			while self.data[j] > pivot:
				j -= 1

			# If i > j, i and j have crossed, and that's where the partition line is
			# drawn.
			if i <= j:
				self.data[i], self.data[j] = self.data[j], self.data[i]
				i += 1
				j -= 1

		# The partition is now drawn and i is the first number to the right of the partition.
		return i

	def quick_sortr(self, left, right):
		""" Sort the array from left to right. """

		if left < right:
			q = self.partition(left, right)

			# q returns the number to the right of the partition line, so q must be
			# decremented to include only the numbers to the left of the partition.
			self.quick_sortr(left, q - 1)
			self.quick_sortr(q, right)

	def quick_sort(self):
		""" Sorts an array using quick sort. """

		# Defines self.size without changing the class itself.
		self.quick_sortr(0, self.size - 1)

	def check_order(self):
		""" Checks to see if the array is in ascending order. """

		for i in range(1, self.size - 1):
			# Note that number may be greater than OR equal to the one before it in order 
			# to NOT return false.
			if self.data[i] < self.data[i - 1]:
				return False

		return True

	def check_sort(self):
		""" Prints a message stating whether or not the array is in order. """

		if self.check_order():
			print('Checked - Array is sorted')
		else:
			print('Checked - Array is NOT sorted')

	def test_return(self):
		""" Returns 'Pass' or 'Fail' depending on if the array is in order. """

		if self.check_order():
			return('Pass')
		else:
			return('Fail')

	def print(self, msg=None, columns_per_row=10):
		""" Print the current state of the array. """

		if msg:
			print()
			print(f'{msg}')
			print()

		for i in range(self.size):
			print(f'{self.data[i]:9d}', end="")

			# Prints the data in a grid format by starting a new row each time
			# COLUMNS_PER_ROW number of characters have been printed
			if (i + 1) % columns_per_row == 0:
				print()
