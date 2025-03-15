function containsDuplicate(nums: number[]): boolean {
    let numsSet = new Set<number>()

    for (let num of nums){
        if(numsSet.has(num)){
            return true
        }
        numsSet.add(num)
    }
    return false
    // let counter = {}

    // for (let num of nums){    
    //     if(counter[num] == 1){
    //         return true
    //     }
    //     counter[num] = 1
    // }
    
    // return false
};