# Remove the outer parentheses from the results of assoc_r 
def assoc(lst):
	if len(lst) == 1: 
		return [lst]
	else:
		rslt = assoc_r(lst)
		return [x[1:-1] for x in rslt]

# Generate a list of all groupings by spitting the list,
# recursing to construct groupings for each half 
# then reassembling corresponding pairs
def assoc_r(lst):
	if len(lst) == 1: 
		return lst
	else:
		result = []
		for i in range(1, len(lst)):
			left = assoc_r(lst[:i])
			right = assoc_r(lst[i:])
			result = result + ['('+ ''.join([x, y]) +')' for x in left for y in right]
		return result
