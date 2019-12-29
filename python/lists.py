# Learn how to use basic list operations like
# insert, remove, pop, reverse, append, and sort.

if __name__ == '__main__':
    N = int(input())
    list = []

    for command in range(0, N):
        instruction = input().split()

        if len(instruction) == 3:
            list.insert(int(instruction[1]), int(instruction[2]))
        elif len(instruction) == 2:
            if instruction[0] == 'remove':
                list.remove(int(instruction[1]))
            elif instruction[0] == 'append':
                list.append(int(instruction[1]))
        elif len(instruction) == 1:
            if instruction[0] == 'print':
                print(list)
            elif instruction[0] == 'sort':
                list.sort()
            elif instruction[0] == 'reverse':
                list.reverse()      # reverse a list, not sort
            elif instruction[0] == 'pop':
                list.pop()  # removes and returns last value from the list

