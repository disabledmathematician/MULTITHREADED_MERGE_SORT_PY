
from multiprocessing.pool import ThreadPool

# Charles Truscott Watters
# Thank you Eric Grimson, John Guttag, Ana Bell
# Multithreaded Merge Sort in Python
def sort(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result
	
def merge(L):
	if len(L) < 2:
		return L[:]
	else:
		mid = len(L) // 2
		left = merge(L[:mid])
		right = merge(L[mid:])
		pool = ThreadPool(processes=6)
		result = pool.apply_async(sort, (left, right))
		ans = result.get()
		return ans

ans = merge([x for x in range(1000, 0, -1)])
print(ans)	