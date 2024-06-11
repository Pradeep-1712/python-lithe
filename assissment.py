print("Assignment 1")
for i in range(0,5):
    print("* * * * *")

print("\nAssignment 2")

def triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

n = 5
triangle(n)

print("\nAssignment 3")

def cross(n):
    for i in range(n):
        for j in range(n):
            # we are checking if i and j have same vaules 
            # or if i added with j gives same value as n-1
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

square(5)
inversePeramid(2)
cross(3)