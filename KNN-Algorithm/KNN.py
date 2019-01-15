from random import randrange, seed
from math import sqrt, ceil

dataset = []
counter = 0
correct = wrong = 0
tp = fp = fn = tn = 0
correctSum = 0.0
prec = rec = 0.0


def main():
    readFile()
    # FoldDataset()
    crossValidation()
    Accuracy(correctSum, 10, 2)
    precision()
    recall()
    f_measure()


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
    right = 0
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

        if cls1 > cls2:
            predict.append([Acls, 1])
        else:
            predict.append([Acls, 2])

        global correct, wrong, tp, fp, tn, fn

        # Let's assume class value:1 -> positive    class value:2 -> negative
        # predict[c][0] -> Actual class     predict[c][1] -> Predicted class

        if predict[c][0] == predict[c][1] == 1:
            correct += 1
            right += 1
            tp += 1
        elif predict[c][0] == predict[c][1] == 2:
            correct += 1
            right += 1
            tn += 1
        elif predict[c][0] == 2 and predict[c][1] == 1:
            fp += 1
        elif predict[c][0] == 1 and predict[c][1] == 2:
            fn += 1
        c += 1

    Accuracy(right, ceil(counter / 10.0), 1)



def Accuracy(ctotal, n, flag):
    if flag == 1:
        print("Total correct prediction: ", ctotal, "\tnumber of data: ", n)
        result = float(ctotal * 100.0 / n)
        global correctSum
        correctSum += result
    else:
        print("Total accuracy of 10 folds: ", ctotal, "\tnumber of data: ", n)
        result = float(ctotal / n)

    print(result)
    print("Accuracy of prediction: %.2f%%" % result)


def precision():
    global prec
    prec = float(tp / (tp + fp))
    print("Precision: %.3f" % prec)


def recall():
    global rec
    rec = float(tp / (tp + fn))
    print("Recall: %.3f" % rec)


def f_measure():
    f = 2 * (prec * rec / (prec + rec))
    print("F-measure: %.3f" % f)


if __name__ == '__main__':
    main()
