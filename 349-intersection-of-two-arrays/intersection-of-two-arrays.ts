function intersection(nums1: number[], nums2: number[]): number[] {
    const hashSet = new Set<number>(nums1)
    const result = []

    for (let num of nums2){
        if (hashSet.has(num)){
            result.push(num)
            hashSet.delete(num)
        }        
    }
    return result
};