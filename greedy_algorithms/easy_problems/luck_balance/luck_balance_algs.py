

def getMaxLuckBalanceBruteForceApproach(lossLimit: int, contests: list) -> int:
    importantLuck, unimportantLuck = filterContestsIntoTwoLists(contests)
    maxLuckTotal: int = 0

    for _ in range(lossLimit):
        if len(importantLuck) > 0:
            maxLuckTotal += max(importantLuck)
            importantLuck.remove(max(importantLuck))

    maxLuckTotal += sum(unimportantLuck) - sum(importantLuck)
    return maxLuckTotal


def filterContestsIntoTwoLists(contests: list) -> tuple:
    luckBalanceFilter: LuckBalanceFilter = LuckBalanceFilter(contests)
    luckBalanceFilter.filter()

    importantLuck: list = luckBalanceFilter.importantLuckBalances
    unimportantLuck: list = luckBalanceFilter.unimportantLuckBalances

    return importantLuck, unimportantLuck


class LuckBalanceFilter():

    def __init__(self, contests: list):
        self.contests: list = contests
        self.importantLuckBalances: list = []
        self.unimportantLuckBalances: list = []

    def filter(self):
        for luckBalance, contestImportance in self.contests:
            if contestImportance == 1:
                self.importantLuckBalances.append(luckBalance)
            else:
                self.unimportantLuckBalances.append(luckBalance)


if __name__ == "__main__":
    pass
