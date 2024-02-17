from threading import Thread, Lock
# Charles Truscott Watters
# Thank you Eric Grimson, John Guttag, Ana Bell
# My try at a multithreaded Merge Sort in Python
def sort(left, right, result):
	i, j = 0, 0
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
		lock = Lock()
		lock.acquire()
		result = []
		threads = [Thread(target=sort, args=(left, right, result)), Thread(target=sort, args=(left, right, result)), Thread(target=sort, args=(left, right, result))]
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()
		lock.release()
		return result
		
		