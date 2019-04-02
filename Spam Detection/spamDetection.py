from random import randrange, seed
from math import sqrt, ceil


def main():
    filename = "spambase.data"
    dataset = readfile(filename)
    pSpamWord, pNonspamWord = trainData(dataset)
    # print(pSpamWord, pNonspamWord)
    crossValidation(dataset, pSpamWord, pNonspamWord)


def readfile(filename):
    file = open(filename, "r+")
    fullData = file.readlines()
    dataset = []
    for line in fullData:
        line = line.split(',')
        line = [float(x) for x in line]
        dataset.append(line)
    print(len(dataset), " ", len(dataset[1]))
    print(dataset[1])
    return dataset


def trainData(dataset):
    spamMail, nonspamMail = 0, 0
    for line in dataset:
        if(line[-1]) == 1.00:
            spamMail += 1
        else:
            nonspamMail += 1

    print(spamMail, "\t", nonspamMail)
    pSpamWord = [0 for x in range(len(dataset[0]) - 1)]
    pNonspamWord = [0 for x in range(len(dataset[0]) - 1)]

    # total = len(dataset)
    for i in range(len(dataset[0]) - 1):
        spamCount, nonspamCount = 0, 0
        for line in dataset:
            if(line[-1]) == 1.00:
                spamCount += 1
            else:
                nonspamCount += 1
        pSpamWord[i] = float(spamCount) / (spamCount + nonspamCount)
        pNonspamWord[i] = float(nonspamCount) / (spamCount + nonspamCount)
        # print("spam + nonspam: "spamCount + nonspamCount)
    return pSpamWord, pNonspamWord


def crossValidation(dataset, pSpamWord, pNonspamWord):
    seed(90)
    accuracy = 0
    for _ in range(0, 10):
        test = []
        train = []
        index = []
        for _ in range(0, ceil(len(dataset) / 10.0)):
            # for _ in range(0, 2):
            i = randrange(0, len(dataset))
            index.append(i)
            test.append(dataset[i])

        for i in range(0, len(dataset)):
            if i not in index:
                train.append(dataset[i])

        recentAccuracy = checkTestset(test, pSpamWord, pNonspamWord)


def checkTestset(test, pSpamWord, pNonspamWord):
    '''
    CHECK
    '''


if __name__ == "__main__":
    main()
