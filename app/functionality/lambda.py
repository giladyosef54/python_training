from functools import reduce

a, b = 0, 1
i = 1

fib = lambda n: n if n == 0 or n == 1 else fib(n - 1) + fib(n - 2)
sign_bisect = lambda arr: [filter(lambda num : num < 0, arr)] + [filter(lambda num : num > 0, arr)]


def main():
    print(fib(5))


if __name__ == '__main__':
    main()