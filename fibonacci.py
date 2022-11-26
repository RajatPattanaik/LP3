#Time complexity = O(n)
#Space Complexity = O(1)

a = 0
b = 1
n=int(input("Enter the number of terms in the sequence: "))
print("Fibonacci Series:", end=" ")
if n == 1:
    print(a)
elif n < 1:
    print(' ')
else:
    print(a,b,end=" ")
    while(n-2):
        c=a+b
        a,b = b,c
        print(c,end=" ")
        n=n-1
