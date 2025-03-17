function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) return false

    const counterOne = {}
    const counterTwo = {}

    for (let str of s){
        counterOne[str] = (counterOne[str] || 0) + 1
    }

    for (let str of t){
        counterTwo[str] = (counterTwo[str] || 0) + 1
    }

    for (let key in counterOne){
        if(!counterTwo[key] || counterTwo[key] !== counterOne[key]){
            return false
        }
    }
    return true
};