def remove_element(N, K, A):
    while len(A) > 1:
        found_pair = False
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] <= K:
                    A.pop(j)
                    found_pair = True
                    break
            if found_pair:
                break
        if not found_pair:
            break   
    return "YES" if len(A) == 1 else "NO"
N = int(input("Plz enter the size of the array N: "))  
K = int(input("Plz enter the constant K: "))  
A = list(map(int, input("Plz enter the array A (space-separated integers): ").split())) 
print(remove_element(N, K, A)) 
