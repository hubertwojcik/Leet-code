function findRestaurant(list1: string[], list2: string[]): string[] {
    const listOneMap: Record<string, number> = {}
    const result = []
    let minSum = Infinity

    for ( let i = 0; i < list1.length; i++){
        listOneMap[list1[i]] = i
    }

    for (let i = 0 ;i<list2.length; i++){        
        if (list2[i] in listOneMap){
            const sumIndex = listOneMap[list2[i]] + i
            if(sumIndex < minSum){
                minSum = sumIndex;
                result.length = 0;
                result.push(list2[i])
            }else if(sumIndex===minSum){
                result.push(list2[i])

            }
        }
    }

    return result
};