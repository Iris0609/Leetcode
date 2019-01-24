## implement sort in Python
class Sort():

## 1. Selection Sort
'''
##Idea: find the minimum in the list and swap with the first item of unsort part in the list
##Selction Sort is not a fast sorting algorithm because it uses nested loop to sort; It's useful 
for small data set
## Time: O(n^2)
'''
	def selection_sort(self, A):
		# A -- list
		for i in range(len(A)-1):
			minimum=A[i]
			mini_ind=i
			for j in range(i+1,len(A)):
				if A[j]<minimum:
					minimum=A[j]
					mini_ind=j
			if i!=mini_ind:
				A[i],A[mini_ind]=minimum,A[i]
		return A

## 2. Heap Sort
## Time: O(n*logn) Space: O(n) (In-place Heap Sort is O(1))

## 3. Mergesort
'''
##Idea: keep divided the list to many parts, each time sort and merge two parts into one part; recursive; devide-and -conquer
## very efficient for large data sets
## Time: O(n*logn) 
'''
	def mergesort(self, A):
		
		def merge(A,s,mid,e):
			L=A[s,mid]
			R=A[mid,e]
			i=0
			j=0
			for k in range(s,e+1):
				if L[i]<R[j]:
					A[k]=L[i]
					i+=1
				else:
					A[k]=R[j]
					j+=1

		## divide function
		def mergesort2(A,s,e):
			#s-start
			#e-end
			if s<e:
				mid=(s+e)//2
				mergesort2(A,s,mid)
				mergesort2(A,mid+1,e)
				merge(A,s,mid,e)

		mergesort(A,0,len(A)-1)
		return A

## 4. Insertion Sort
'''
##Idea: insert 1 element to the right place in the prior list each time
##Insertion Sort is not a fast sorting algorithm because it uses nested loop to sort; It's useful 
for small data set
##On arrays with a small number of inversions, insertion sort is extremely fast. 
Less obvious: For small arrays (N < 15 or so), insertion sort is fastest.
## Time: O(n^2) Space: O(n)
'''
	def insertion_sort(A):
		for i in range(1,len(A)):
            curval=A[i]
            curind=i
            while curind>0 and A[curind-1]>curval:
                A[curind]=A[curind-1]
                curind-=1
            A[curind]=curval
        return(A)
## 5. Quick Sort
'''
##Idea: partition, find a pivot, put the smaller number to the left and larger number to the right; recursive; devide-and -conquer
## very efficient for large data sets
## Performance depend largerly on the pivot selection
## Time: O(nlogn) (Worst Case: O(n^2))
'''

	def quick_sort(A):
		def partition(A,s,e):
			pivotIndex=get_pivot(A,s,e)# ge_pivot is a function return pivot index. We compare the s,mid,e element and choose the median as the pivot
			pivotVal=A[pivotIndex]
			A[pivotIndex],A[s]=A[s],pivotVal
			border=s

			for i in range(s,e+1):
				if A[i]<pivotVal:
					# first +1 then swap is because the initial border=s not s+1
					border+=1
					A[border],A[i]=A[i],A[border]
			A[s],A[border]=A[border],A[s]
			return border


		def quick_sort2(A,s,e):
			if e-s<15 and s<e:
				insertion_sort(A,s,e)# when size<15 used insertion sort
			elif s<e:##means there is more than one element need to be sorted 
				p=partition(A,s,e)
				quick_sort2(A,s,p-1)
				quick_sort2(A,p+1,e)
		quick_sort2(A,0,len(A)-1)
		return A


## 6. Bubble Sort
'''
## Idea:

'''

	def bubble_sort(A):
		for i in range(len(A)-1):
			for j in range(len(A)-i-1):
				if A[j]>A[j+1]:
					A[j+1],A[j]=A[j],A[j+1]
		return A




