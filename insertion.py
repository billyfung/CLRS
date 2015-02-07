#Insertion sort
#input: array of length n
#output: sorted array from smallest to largest
def insertion(array):
	length = len(array)
	for j in range(length):
		key = array[j]
		i = j - 1
		while (i>-1 and array[i]>key):
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
	return array

array = [31, 41, 59, 26, 41, 58]
print("The unsorted array is %s: " % array)
insertion(array)
print("The ascending array is %s: " % array)

#largest to smallest
def reverseinsertion(array2):
	length = len(array)
	for j in range(length):
		key = array[j]
		i = j - 1
		while (i>-1 and array[i]<key):
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
	return array

reverseinsertion(array)
print("The descending array is: %s" % array)

#lienar search for index of key in array
def linear(array, key):
	for i in range(len(array)):
		if array[i] == key:
			return i

i=41
print(linear(array,i))

