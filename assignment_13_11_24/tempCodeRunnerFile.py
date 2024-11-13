def can_reduce_to_one_element():
#     num_tests = int(input())  # number of test cases
#     for _ in range(num_tests):
#         # read number of elements and  threshold value
#         num_elements, threshold = map(int, input().split())
#         elements = list(map(int, input().split()))
        
#         # If there is only one element, it's trivially "YES"
#         if num_elements == 1:
#             print("YES")
#             continue
        
#         # Sort the list to easily check the smallest two elements
#         elements.sort()
        
#         # Check if the sum of the two smallest elements is <= threshold
#         if elements[0] + elements[1] <= threshold:
#             print("YES")
#         else:
#             print("NO")

# can_reduce_to_one_element()