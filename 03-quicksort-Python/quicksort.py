"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[high] = array[high], array[i+1]
	return i+1

def quick_sort(array, low, high):
	if low < high:
		p = partition(array, low, high)
		quick_sort(array, low, p - 1)
		quick_sort(array, p + 1, high)

def quicksort(array):
	# Your code goes here
	l = len(array)
	quick_sort(array, 0, l - 1)

	return array

print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))