def summaryRanges(nums: list):
    result = []
    if len(nums) == 0:
        return result
    a = nums[0]
    res = a
    i = 1
    while i < len(nums):
        if nums[i] == res + 1:
            res += 1
            i += 1
        else:
            if a == res:
                result.append("%d" % a)
            else:
                result.append("%d->%d" % (a, res))
            a = nums[i]
            res = a
            i += 1
    if a == res:
        result.append("%d" % a)
    else:
        result.append("%d->%d" % (a, res))
    return result

test = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(test))