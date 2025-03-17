function singleNumber(nums: number[]): number {
    let ones = 0, twos = 0

    for (let num of nums){
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones
    }
    return ones
};