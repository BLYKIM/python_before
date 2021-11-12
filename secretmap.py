def solution(n, arr1, arr2):
    answer = []
    b1 = []
    b2 = []
    for i in arr1:
        b1.append(bin(i).zfill(5))
    for i in arr2:
        b2.append(bin(i))
    print(b1)
    print(b2)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))