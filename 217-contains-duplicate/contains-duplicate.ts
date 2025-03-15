function containsDuplicate(nums: number[]): boolean {
    let counter = {}

    for (let num of nums){    
        if(counter[num] == 1){
            return true
        }
        counter[num] = 1
    }
    
    return false
};