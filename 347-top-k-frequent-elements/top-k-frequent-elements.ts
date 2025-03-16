function topKFrequent(nums: number[], k: number): number[] {
    const counter = {}
    const freq = Array.from({length:nums.length + 1},()=>[])

    for (let num of nums){
        counter[num] = (counter[num] || 0) + 1
    }
    for (let key of Object.keys(counter)){
        freq[counter[key]].push(key)
    }

    const result: number[] = [];
    
    for (let i = freq.length-1; i >=0 ; i --){
        
       for (let num of freq[i]) {
            result.push(Number(num));
            if (result.length === k) return result;
        }

        if(result.length ==k){
            return result
        }
    }

    return result
};