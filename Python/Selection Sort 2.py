# 2nd coding
#A=['t','u','t','o','r','i','a','l']
A=[56,3,19,-1000,6,0,5,-100]
for i in range (len(A)):
    min_=i
    for j in range(i+1, len(A)):
        if A[min_] > A[j]:
            min_=j
            #swap
    A[i], A[min_]= A[min_], A[i]

for i in range (len(A)):
    print(A[i])