## Read an integer n. For all non-negative integers i < N, print i^2.

if __name__ == '__main__':
    n = int(input())

    for index in range(n):
        print(index**2)
