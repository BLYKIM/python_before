def solution(nums):
    answer = 0
    n = len(nums)
    newnums = []
    half = n / 2
    for i in nums:
        if not i in newnums:
            newnums.append(i)
    if len(newnums) > half:
        newnums = newnums[:int(half)]
    answer = len(newnums)

    return answer


nums = [3, 3, 3, 3, 3, 3, 3, 3]
print(solution(nums))

'''
def solution(nums):
    return min(len(nums)/2, len(set(nums)))  # 고유값이 n/2보다 적으면 고유값, 많으면 절반
'''