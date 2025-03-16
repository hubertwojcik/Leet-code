function topKFrequent(words: string[], k: number): string[] {
    const counter = new Map();
    const freq = Array.from({length:words.length+1}, ()=>[])

    for (let str of words){        
        if(counter.has(str)){
            const currentValue = counter.get(str)
            counter.set(str,currentValue+1)
        }else{
            counter.set(str,1)
        }
    }

     for (let [word, count] of counter) {
        freq[count].push(word);
    }
    
    const result:string[] = []

    for ( let i = words.length - 1; i>=0 ; i--){
            if (freq[i].length > 0) {
            
            freq[i].sort();
            for (let str of freq[i]) {
                result.push(str);
                if (result.length === k) return result;
            }
        }
    }

    return []
};