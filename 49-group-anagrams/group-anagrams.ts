function groupAnagrams(strs: string[]): string[][] {
    const wordsMap = new Map<string, string[]>();
    const result = []
    
    for (let str of strs){
        const sortedWord = str.split('').sort().join('')
        console.log(str)
        if(wordsMap.has(sortedWord)){
           wordsMap.get(sortedWord).push(str)
        }else{
        wordsMap.set(sortedWord,[str])
        }
    }
    
    for (const words of wordsMap.values()){
        result.push(words)
    }

    return result
};