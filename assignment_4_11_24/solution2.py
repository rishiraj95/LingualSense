# First thing is to get the number of test cases T
T = int(input())

# After that for each test case run the code
for _ in range(T):

    # Now get the size of the array 
    N = int(input())
    
    # Now we need the elements
    A = list(map(int, input().split()))
    
    # Find the minimum value from the array and store it in M
    M = min(A)
    
    # The next thing will be to count the number of elements greater than minimum and increment it by 1
    count = 0
    for i in A:
        if i > M:
            count += 1
    
    # print the count value in the end
    print(count)

    #end of program

    
