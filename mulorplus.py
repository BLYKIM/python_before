nums = input()
sum = int(nums[0])

for i in range(1, len(nums)):
    num = int(nums[i])
    if num <= 1 or sum <= 1:
        sum += num
    else:
        sum *= num

print(sum)
