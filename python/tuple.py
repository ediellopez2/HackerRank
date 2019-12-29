# Given an integer, n, and n space-separated integers as input, create
# a tuple, t, of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(list(map(int, input().split())))

    print(hash(integer_list))  # encode the data into unrecognisable value

