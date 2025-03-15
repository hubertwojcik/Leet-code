function maxProfit(prices: number[]): number {    
    let minPrice = Infinity
    let maxProfit = 0 

    for (let price of prices){
            if(price < minPrice){
                minPrice = price
            }else{
                maxProfit = Math.max(maxProfit, price - minPrice)
            }
    }
    return maxProfit
};