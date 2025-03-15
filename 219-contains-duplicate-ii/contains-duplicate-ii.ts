function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const windowSet = new Set()
    let left = 0

    for (let right = 0; right < nums.length; right++){
        if((right - left) > k ){
            windowSet.delete(nums[left])
            left+=1        
        }
        if(windowSet.has(nums[right])){
            return true
        }
        windowSet.add(nums[right])
    }
    return false
};