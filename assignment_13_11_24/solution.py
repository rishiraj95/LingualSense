def single_array_reduce(test_case):
    result = []
    for n, k, arr in test_case:
        if n == 1:             # For only one element 
            print("Yes")
        else:
            arr.sort()
            small_num_sum = arr[0] + arr[1]
            if small_num_sum <= k:
                print("Yes")
            else:
                print("No")
    return result


# Input reading
No_of_test_cases = int(input("Enter number of test cases: "))
test_cases = []

for i in range(No_of_test_cases):
    n, k = map(int, input("Enter n and k value: ").split())
    arr = list(map(int, input("Enter array: ").split()))
    test_cases.append((n, k, arr))

result = single_array_reduce(test_cases)
print("\n".join(result))