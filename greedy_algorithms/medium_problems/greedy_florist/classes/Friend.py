

class Friend:

    def __init__(self):
        self.purchase_count: int = 0

    def get_flower_cost_at(self, price: int) -> int:
        flower_cost = (self.purchase_count + 1) * price
        self.purchase_count += 1
        return flower_cost
