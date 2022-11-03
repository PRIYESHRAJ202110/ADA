# Implement Merge Sort
# Merge Sort is based on the principle of Divide and Conquer Algorithm

from array import array


def MergeSort(A):
    if len(A) > 1:

        # The array is divided into two subarrays
        r = len(A) // 2
        L = A[:r]
        M = A[r:]

        # Sort the two halves
        MergeSort(L)
        MergeSort(M)
        
        # Index for the main array and two subarrays 
        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among the
        # elements in L and M and place them in the correct position at A[p..r]
        while(i < len(L) and j < len(M)):
            if L[i] < M[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = M[j]
                j += 1
            
            k += 1

        # When one of the subarrays reaches its end
        # copy the remaining part of the other subarray  
        while(i < len(L)):
            A[k] = L[i]
            i += 1
            k += 1
        
        while(j < len(M)):
            A[k] = M[j]
            j += 1
            k += 1

# Driver code
array = [6, 5, 12, 10, 9, 1]
MergeSort(array)
print('Sorted array is:', array, sep='\n')