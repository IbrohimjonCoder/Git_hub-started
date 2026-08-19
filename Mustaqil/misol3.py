def rearrange_by_frequency(nums: list[int]) -> list[int]:
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    unique_nums = list(set(nums))

    unique_nums.sort()
    
    unique_nums.sort(key=lambda x: count_dict[x], reverse=True)
    

    result = []
    for num in unique_nums:
        sanoq = count_dict[num]
        result.extend([num] * sanoq)

    return result

print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))