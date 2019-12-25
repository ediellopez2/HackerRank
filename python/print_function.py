##  Read an integer n.
##  
##  Without using any string methods, try to print the following:
##  
##  123.....n


def foo(n):
    for index in range(1, n+1):
        print(index, end='')

if __name__ == '__main__':
    n = int(input())

    foo(n)
