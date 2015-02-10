#mergesort implementation with recursion 
#mergsort(A,p,r) ~ A[p,r]
#input: A-array to be sorted
#		p-element p 
#		r-element r

def merge(A,p,q,r):
	n1 = q - p +1
	n2 = r - q
	for i in n1:
		L[i]􏰀 = A[p + i 􏰐-1]
	for j in n2:
		􏰀R[j] = A[q+j]
	L[n1+1] = 
	R[n2+1] = 
	i = 1
	j = 1
	for k in range(p,r):
		if L[i]􏰀 􏰎<= R[j]:
			A[k] = L[i]
			i = i +1
		else:
			A[k] = R[j]
			j = j + 1
􏰀


def mergesort(A,p,r):
	if p < r:
		q = ((r+p)/2) #q is the midpoint 
		mergesort(A,p,q)
		mergesort(A,q+1,r)
		merge(A,p,q,r)