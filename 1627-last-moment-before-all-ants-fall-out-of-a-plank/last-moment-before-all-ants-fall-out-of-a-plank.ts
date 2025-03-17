function getLastMoment(n: number, left: number[], right: number[]): number {
    let maxTime = 0

    for (let pos of left){
        maxTime= Math.max(maxTime, pos)
    }

        for (let pos of right){
        maxTime= Math.max(maxTime, n - pos)
    }

    return maxTime
};