# The skip_elements function returns a list containing every other element from an input list, starting with the
# first element. Complete this function to do that,
# using the for loop to iterate through the input list.

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements): 
		if index % 2 == 0:
			new_list.append(element)

	
	return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([]))  # Should be []
