def fib(n):
    first = next = 1
    yield first
    yield next
    for i in range(2, n):
        first, next = next, first + next
        yield next