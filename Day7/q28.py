def fibonacci(a):
    """Recursive function to print fibbonacci series"""
    if (a<=1):
        return a
    else:
        return (fibonacci(a-1)+fibonacci(a-2))




n=5
for i in range(n):

    print(fibonacci(i))

