import math


def main():
    classes, dataset = extractClass()
    print(classes)
    print()
    initialEntropy = entropyInDataset(dataset, classes)
    root = splitData(dataset, initialEntropy)
    #splitData(dataset, initialEntropy)


def extractClass():
    file = open("iris.txt", "r+")
    fullData = file.readlines()
    dataset = []
    classSet = set()
    for line in fullData:
        line = line.split(',')
        dataset.append(line)
        classSet.add(int(line[-1]))

    return classSet, dataset


def entropyInDataset(dataset, classes):
    totalData = len(dataset)
    print(totalData)

    entropy = 0.0
    for value in classes:
        occurences = [int(row[-1]) for row in dataset].count(value)
        print(occurences)
        probability = occurences / totalData
        #print(probability)
        #print(math.log2(probability))
        entropy += (-probability * math.log2(probability))
        print(entropy)
    return entropy


def splitData(dataset, initialEntropy):
    indices = len(dataset[0])
    print(indices)
    leftSet, rightSet = list(), list()

    for row in dataset:
        for index in range(indices - 1):
            leftSet, rightSet = getTwoSet(dataset, index, float(row[index]))

    root = None
    return root


    
def getTwoSet(dataset, index, indexValue):
    leftSet, rightSet = list(), list()

    for row in dataset:
        if float(row[index]) < indexValue:
            leftSet.append(row)
        else:
            rightSet.append(row)

    return leftSet, rightSet


if __name__ == "__main__":
    main()