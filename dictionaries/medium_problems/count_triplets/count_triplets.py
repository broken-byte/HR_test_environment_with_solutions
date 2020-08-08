from collections import Counter

def countTriplets(arrayOfNumbers, ratio):

    potentialJs = Counter()
    potentialKs = Counter()

    numberOfGeoTriplets = 0

    for number in arrayOfNumbers:

        if number in potentialKs:
            '''
            Number exists in potentialKs bag! 
            That means that we've found a triplet! 
            Let's increment the numberOfGeoTriplets 
            by how many times its "progessed" to this 
            point (the number of times its appeared in the bag)...
            '''
            numberOfGeoTriplets += potentialKs[number]

        if number in potentialJs:
            '''
            The number exists in the potentialJs bag! 
            That means that we are on our way to a 
            potential geoTriplet...Let's add/increment 
            it's progression to the potentialKs bag with
            a number of instances equal to how many times 
            its appeared in the potentialJs. 
            '''
            nextGeoProgression = number * ratio

            potentialKs[nextGeoProgression] += potentialJs[number]

        '''
        Regardless of whether it exists in either bag, 
        it can always potentially be the start of a geometric 
        progression so let's add it's nextGeoProgession to 
        the potentialJs...
        '''
        nextGeoProgression = number * ratio

        potentialJs[nextGeoProgression] += 1

    return numberOfGeoTriplets

def main():
    testArr1 = [1,4,16,64]
    testRatio1 = 4

    testArr2 = [1,2,2,4]
    testRatio2 = 2

    countTriplets(testArr2, testRatio2)

if __name__ == "__main__":
    main()
