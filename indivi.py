def solution(nums):
    answer = 0
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i < j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    for n in range(2, sum):
                        if sum % n == 0:  # 소수가 아닌 경우
                            break
                        if n == sum - 1:  # 소수인 경우
                            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]

print(solution(nums))
