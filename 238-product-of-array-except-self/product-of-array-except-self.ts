function productExceptSelf(nums: number[]): number[] {
    const result = []
    let prefix = 1

    for (let i = 0; i < nums.length; i ++){
        result[i] = prefix
        prefix*=nums[i]
    }

    let postfix = 1
    for (let i = nums.length - 1 ; i>=0 ; i --){
        result[i]*= postfix
        postfix *= nums[i]
    }
    return result
};