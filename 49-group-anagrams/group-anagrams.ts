function groupAnagrams(strs: string[]): string[][] {
    const hashMap = new Map<string,string[]>();

    for (let str of strs){
       const sortedStr = str.split('').sort().join('');
        
        if (hashMap.has(sortedStr)){
            hashMap.get(sortedStr)!.push(str);
        } else {
            hashMap.set(sortedStr, [str]);
        }
    }
    
    return Array.from(hashMap.values())
};