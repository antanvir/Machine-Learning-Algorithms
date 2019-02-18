import math


def main():
    classes, dataset = extractClass()
    # print(dataset)
    # print()
    initialEntropy = entropyInDataset(dataset, classes)
    root = splitData(dataset, initialEntropy, classes)
    print(root)
    #splitData(dataset, initialEntropy)


def extractClass():
    file = open("iris1.txt", "r+")
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
    # print(totalData)
    if totalData == 0:
        return 0.0

    entropy = 0.0
    for value in classes:
        occurences = [int(row[-1]) for row in dataset].count(value)
        print(occurences)
        probability = occurences / totalData
        # print(probability)
        # print(math.log2(probability))
        if probability > 0.0:
            entropy += (-probability * math.log2(probability))
            print(entropy)
    return entropy


def GetInformationGain(leftSet, rightSet, classes, initialEntropy):
    infoGain = 0.0
    entropy = 0.0
    total = len(leftSet) + len(rightSet)

    entropy += (len(leftSet) / total) * entropyInDataset(leftSet, classes)
    entropy += (len(rightSet) / total) * entropyInDataset(rightSet, classes)

    infoGain = initialEntropy - entropy
    return infoGain


def splitData(dataset, initialEntropy, classes):
    indices = len(dataset[0])
    # print(indices)
    leftSet, rightSet = list(), list()

    print("Splitting....")
    gainValue = 0.0
    position, value, left, right = -1, -1, None, None
    for row in dataset:
        for index in range(indices - 1):
            leftSet, rightSet = getTwoSet(dataset, index, float(row[index]))
            infoGain = GetInformationGain(
                leftSet, rightSet, classes, initialEntropy)
            if infoGain > gainValue:
                position, value, left, right = index, row[index], leftSet, rightSet

    root = {"index": position, "value": value, "left": left, "right": right}
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
