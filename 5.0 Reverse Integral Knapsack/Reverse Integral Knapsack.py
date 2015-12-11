
import numpy as np

#input: 
# n objects
# v{i} value of object i (integer)
# s{i} size of object i
# V target value

#output
# set of K objects to go in knapsack with total value >= V,
#   to minimize the total of size of the knapsack required

def reverse_integral_knapsack(n, values, sizes, V):
	memo = np.zeros((n+1,V+1))

	#set base cases
	memo[n,:] = float("inf")
	memo[:,V] = 0

	for j in range(V-1,0-1,-1):
		for i in range(n-1,0-1, -1):
			#print "(i,j)= (" + str(i) + "," + str(j) + ")"
			memo[i,j] = min(memo[i+1,j], memo[i+1,min(j+values[i],V)] + sizes[i])
			#print memo
			
	return memo[0][0], memo



#test example
n = 3
values = [3,4,5]
sizes = [2,5,3]
V = 7

(min_size, memo_table) = reverse_integral_knapsack(n,values,sizes,V)
print "minimum size required to achieve target value: " + str(min_size) +" ; resulting memo table:"
print memo_table
