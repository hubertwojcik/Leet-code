function topKFrequent(nums: number[], k: number): number[] {
    const counter  = {}
    const freq = Array.from({length:nums.length + 1},()=>[])

    for (let num of nums){
        counter[num] = (counter[num] || 0) + 1
    }   
    for (let key in counter){        
        freq[counter[key]].push(Number(key))        
    }

    const result = []
    
    for (let i = nums.length; i >= 0; i--){
            for (let num of freq[i]){
                result.push(num)
                if(result.length == k){
                    return result
                }
            }
    }

    

  

};