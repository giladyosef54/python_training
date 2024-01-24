fib = lambda n: n if n == 0 or n == 1 else fib(n - 1) + fib(n - 2)
sign_bisect = lambda arr: [filter(lambda num : num < 0, arr)] + [filter(lambda num : num > 0, arr)]


