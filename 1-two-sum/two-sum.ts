function twoSum(nums: number[], target: number): number[] {
    const counter = {}

    for (let i = 0; i < nums.length; i++){
        if ((target - nums[i]) in counter){            
            return [i, counter[target - nums[i]]]
        }
        counter[nums[i]] = i
    }

    return []
};