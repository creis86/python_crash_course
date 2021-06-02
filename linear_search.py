
def linear_search(array, key):
    for i in range(0, len(array)):
        if array[i] == key:
            return i


def binary_sum(A, B):
    n = len(A) - 1
    C = [0 for i in range(0, len(A) + 1)] 
    carry = 0

    for i in range(0, len(A)):
        sum = A[n - i] + B[n - i] + carry
        C[n - i + 1] = sum % 2
        if sum <= 1:
            carry = 0
        else:
            carry = 1

    C[0] = carry
    return C

A = [1, 0, 0, 0, 1]
B = [1, 0, 1, 1, 0]
C = binary_sum(A, B)
print(C)