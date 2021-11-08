def solution(numbers):
    answer = []
    numbers.sort()
    nums = len(numbers) # numbers의 길이 (2 - 100)

    for i in range(nums):
        for j in range(nums):
            if i != j:
                sum = numbers[i] + numbers[j]
                if not sum in answer:
                    answer.append(sum)

    return answer


numbers = [5, 0, 2, 7]

print(solution(numbers))