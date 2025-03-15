function twoSum(nums: number[], target: number): number[] {
   const numsMap = new Map();

    for(let i = 0; i<nums.length;i++){
            if(numsMap.has(target - nums[i])){
            return [i,numsMap.get(target - nums[i])]
        } 
        numsMap.set(nums[i],i)       
    
    }
    return []
};