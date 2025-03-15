/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    let kr = k % nums.length

    reverse(nums,0 , nums.length - 1)
    reverse(nums, 0 , kr - 1)
    reverse(nums, kr, nums.length - 1 )
};


function reverse(arr:number[], start:number, end: number){
    while (start < end){
        [arr[start], arr[end]] = [arr[end], arr[start]]
        start++
        end--
    }
}
