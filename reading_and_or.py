import numpy as np

def min_unhappiness(m,t):
    
    D = len(m)
    n = len(t)

    memo = np.zeros((D+1,n+1))
    m.insert(0,0) #insert 0 at front of m so days 1...D align with m indices
    t.insert(0,0) #insert 0 at front of t so section 0 takes 0 time

    #base cases
    if n == 0:
        return 0, memo #todo

    memo[0,:] = 0 #no unhappiness from reading j sections within 0 days
    memo[D,0:n] = float("inf") #infinite unhappiness if you don't read section n of K&T by day D
    memo[0,n] = float("inf")

    for i in range(1,D+1):
    	for j in range(0, n+1):

            #on last day, must finish last section
            if i == D and j!=n:
                continue

            min_unhappiness = float("inf")

            for k in range(0,j+1):

                T = sum(t[k+1:j+1]) #minutes spent reading sections k...j-1
                F = max(m[i]-T,0) #free time
                S = max(T-m[i],0) #lost sleep

                #unhappiness from reading sections 1...k by day i-1, and sections k+1...j on day i
                unhappiness = memo[i-1,k] + S + pow(F,4)
                
                min_unhappiness = min(min_unhappiness,unhappiness)

            memo[i,j] = min_unhappiness

    result = memo[D,n]

    if result!= float("inf"):
        result = int(result)
    
    return memo, result

    return 0,0

def run_test(m,t, expected_val):

    print "m:" + str(m)
    print "t:" + str(t)

    memo,min_val = min_unhappiness(m,t)
    
    print "expected value: " + str(expected_val)
    print "minimum unhappiness: " + str(min_val)
    print "resulting memo table: "
    print memo
    print 

if __name__ == "__main__":

    m = [5,4,6]
    t = [3,1,5,4]
    expected_val = 18

    run_test(m,t, expected_val)

    m = [1]
    t = [3]
    expected_val = 2

    run_test(m,t, expected_val)

    m = []
    t = [3]
    expected_val = float("inf")

    run_test(m,t, expected_val)

    m = [8,4]
    t = [3,3]
    expected_val = 272

    run_test(m,t, expected_val)

    m = [1]
    t = [200]
    expected_val = 199

    run_test(m,t, expected_val)

    m = [3,2]
    t = [3]
    expected_val = 16

    run_test(m,t, expected_val)

    m = [6,5]
    t = [4]
    expected_val = 625+16

    run_test(m,t, expected_val)