function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false

    const counterS = {}
    const counterT = {}

    for (let str of s){
        counterS[str] = (counterS[str] || 0) + 1
    }

    for (let str of t){
        counterT[str] = (counterT[str] || 0) + 1
    }

    for (let key of Object.keys(counterS)){
        if(!counterT[key] || counterS[key] !== counterT[key]) return false
    }
    return true

};