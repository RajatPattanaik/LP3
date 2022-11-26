#Time complexity = O(2^n)
#Space Complexity = O(n)

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

n = int(input("Enter a number: "))
if n < 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(recursive_fibonacci(i), end=" ")