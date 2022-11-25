def fibonacciModified(t1, t2, n):
# Write your code here
	arr = [0 for i in range(n)]
	arr[0] = t1
	arr[1] = t2
	for i in range(2,n):
 		arr[i] = arr[i-2]+arr[i-1]**2
	return arr[n-1]

