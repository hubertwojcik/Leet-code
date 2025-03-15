function removeDuplicates(nums: number[]): number {
    if(!nums) return 0

    let k = 0

    for (let i = 0; i < nums.length; i++){

        if (nums[i] !== nums[k]){
            k += 1
            nums[k] = nums[i]
        }

    }
    return k+1

    
};