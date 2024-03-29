A = []
B = []
C = []


def hanoi_towers(n):
    global A

    n = int(n)

    A = list(range(n, 0, -1))
    print_towers()
    get_ht_solution(A, B, C, n)


def print_towers():
    print('towers:')
    print('A:', A, '\nB:', B, '\nC:', C)
    print('---------------------------')


def get_ht_solution(src, aux, dst, n):
    if n > 0:
        get_ht_solution(src, dst, aux, n - 1)
        dst.append(src.pop())
        print_towers()
        get_ht_solution(aux, src, dst, n - 1)
