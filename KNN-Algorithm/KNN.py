from random import randrange, seed
from math import sqrt, ceil

dataset = []
counter = 0
correct = wrong = 0


def main():
    readFile()
    # FoldDataset()
    crossValidation()
    Accuracy()


def readFile():
    file = open("haberman.data", "r+")
    fullData = file.readlines()

    for line in fullData:
        line = line.split(',')
        dataset.append(line)
        global counter
        counter += 1


def crossValidation():
    seed(4)

    for _ in range(0, 10):
        test = []
        index = []
        train = []
        FoldDataset(train, test, index)
        knnAlgo(train, test)


def FoldDataset(train, test, index):
    for _ in range(0, ceil(counter / 10.0)):
        # for _ in range(0, 2):
        i = randrange(0, counter)
        index.append(i)
        test.append(dataset[i])

    for i in range(0, counter):
        if i not in index:
            train.append(dataset[i])


def knnAlgo(train, test):
    predict = []
    c = 0
    for i in test:
        dist_cls = []

        for j in train:
            x = int(i[0]) - int(j[0])
            y = int(i[1]) - int(j[1])
            z = int(i[2]) - int(j[2])
            dst = round(sqrt(x * x + y * y + z * z), 3)
            Tcls = int(j[3])
            Acls = int(i[3])
            dist_cls.append([dst, Acls, Tcls])

        dist_cls.sort()
        cls1 = cls2 = 0

        for x in range(3):
            if dist_cls[x][2] == 1:
                cls1 += 1
            else:
                cls2 += 2

        Acls = int(i[3])
        global correct, wrong

        if cls1 > cls2:
            predict.append([Acls, 1])
        else:
            predict.append([Acls, 2])

        #print(predict[c][0], " ", predict[c][1])
        if predict[c][0] == predict[c][1]:
            correct += 1

        c += 1


def Accuracy():
    print("correct: ", correct, "\ttotal data: ", counter)
    result = float(correct * 100.0 / counter)
    print(result)
    print("Accuracy of prediction: %.2f%%" % result)


if __name__ == '__main__':
	main()
