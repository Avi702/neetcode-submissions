class StockSpanner:

    def __init__(self):
        self.stock = []
    def next(self, price: int) -> int:
        count = 1
        for i in range(len(self.stock)-1,-1,-1):
            if self.stock[i] <= price:
                count +=1
            else:
                self.stock.append(price)
                return count
        self.stock.append(price) 
        return count





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)