
# Driver Function
def frequencyQueries(queries):
    frequencyQueries = FrequencyQueries()
    frequencyQueries.frequencyQueries(queries)
    return frequencyQueries.zArray

class FrequencyQueries:

    def __init__(self):
        self.elementCounter = {}
        self.frequencyCounter = {}
        self.zArray = []

    def frequencyQueries(self, queries):
        for query in queries:
            self.queryCalculator(query)

    def queryCalculator(self, query):
        operationFlag = query[0]
        element = query[1]

        if operationFlag == 1: self.append(element)

        elif operationFlag == 2: self.delete(element)

        elif operationFlag == 3: self.verifyFrequencyOf(element)

    def append(self, x):
        if x not in self.elementCounter:
            self.elementCounter[x] = 1
            self.addFrequency(1)
        else:
            elementFrequency = self.elementCounter[x]
            self.subtractFrequency(elementFrequency)

            self.elementCounter[x] += 1

            elementFrequency = self.elementCounter[x]
            self.addFrequency(elementFrequency)

    def delete(self, y):
        if y in self.elementCounter:
            elementFrequency = self.elementCounter[y]
            self.subtractFrequency(elementFrequency)
            
            self.elementCounter[y] -= 1

            elementFrequency = self.elementCounter[y]
            self.addFrequency(elementFrequency)

            if self.elementCounter[y] == 0:
                self.elementCounter.pop(y)

    def verifyFrequencyOf(self, z):
        if z in self.frequencyCounter:
            if self.frequencyCounter[z] == 0: 
                self.zArray.append(0)
            else: 
                self.zArray.append(1)
        else:
            self.zArray.append(0)

    def addFrequency(self, frequency):
        if frequency not in self.frequencyCounter:
            self.frequencyCounter[frequency] = 1
        else: 
            self.frequencyCounter[frequency] += 1

    def subtractFrequency(self, frequency):
        if frequency in self.frequencyCounter:
            if self.frequencyCounter[frequency] == 0:
                # Do nothing, the frequency is not present in elementCounter
                return
            self.frequencyCounter[frequency] -= 1

def main():
    pass

if __name__ == "__main__":
    main()