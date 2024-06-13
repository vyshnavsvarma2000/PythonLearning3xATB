def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    fib_sequence = [0,1]
    for i in range(2, n+1):
        fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(fib)
    return fib_sequence

print(fibonacci(4))
