function longestCommonPrefix(strs: string[]): string {
    let res = ""

    for (let i = 0; i<strs[0].length; i++){
        for (let str of strs){
            if(i === str.length || str[i] !== strs[0][i] ){
                return res
            }
        }
        res += strs[0][i]
    }
    return res
};