unsorted_list = [20, 7, 3, 4, 12, 15, 2, 1]

def merge(left, right):
	result=[]
	i, j=0,0
	while(i<len(left) and j<len(right)):
		if(left[i]<=right[j]):
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

	result+=left[i:]
	result+=right[j:]
	return result


def mergeSort(a):
	if(len(a)<2):
		return a
	middle=len(a)/2
	left = mergeSort(a[:middle])
	right = mergeSort(a[middle:])

	out = merge(left,right)
	return out

print(unsorted_list)
print(mergeSort(unsorted_list))