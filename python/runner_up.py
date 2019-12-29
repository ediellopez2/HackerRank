
## Given the participants' score sheet for your University Sports Day,
## you are required to find the runner-up score. You are given  scores.
## Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())

    # This method allows you to enter a stream of numbers (ex. 2 3 6 6 5)
    arr = list(map(int, input().split()))

    # Alternative method. Create an empty list. Populate the list with
    # values, one-by-one.
    ##    arr = []
    ##    # Get all of the values
    ##    for index in range(n):
    ##        num = int(input())
    ##        arr.append(num)
        
    # Sort the list in ascending order
    arr.sort()
    
    ## print("sorted array in ascending order: ")
    ##    for index in range(n):
    ##        print(arr[index])

    # The highest value is at the end. So, we shall set the
    # runner_up to the highest value for now. 
    runner_up = arr[-1]

    # Iterate through the list in reverse order. The moment you
    # find a value less than the highest value, you've found the
    # runner up.
    for index in range(n, 0, -1):
        if arr[index-1] < runner_up:
            runner_up = arr[index-1]
            break

    # Print the runner up! 
    print(runner_up)
    
    

