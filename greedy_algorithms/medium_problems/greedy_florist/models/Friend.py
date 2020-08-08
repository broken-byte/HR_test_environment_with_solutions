

class Friend:

    purchaseCount: int = 0

    def __init__(self):
        pass

    def getFlowerCostAt(self, price: int) -> int:
        flowerCost = (self.purchaseCount + 1) * price
        self.purchaseCount += 1
        return flowerCost