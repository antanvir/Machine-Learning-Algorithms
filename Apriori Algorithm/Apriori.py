DELIMITER = ","


def main():
    dataset = readFile()
    L1 = find_frequent_1_itemsets(dataset)
    ItemsetsLevel, ItemsetsCounter = apriori(dataset)
    Print(ItemsetsLevel, ItemsetsCounter)
    given, conFor = Input()
    Confidence(ItemsetsLevel, ItemsetsCounter, given, conFor)


def readFile():
    file = open("transactions.txt", "r+")
    dataset = list()
    while True:
        line = file.readline().strip()
        item = line.split(" ")
        if not line:
            break
        dataset.append(item[1])

    return dataset


def apriori(dataset):
    threshold = 2
    resultLevel = list()
    resultCounter = list()

    candidate = find_frequent_1_itemsets(dataset)
    Level, L_count = has_Minimum_Support_Counter(dataset, candidate, threshold)
    resultLevel.append(Level)
    resultCounter.append(L_count)

    while Level:
        candidate = candidate_generator(Level)
        candidate = has_frequent_subset(candidate, Level)
        Level, L_count = has_Minimum_Support_Counter(
            dataset, candidate, threshold)

        resultLevel.append(Level)
        resultCounter.append(L_count)

    return resultLevel, resultCounter


def has_Minimum_Support_Counter(dataset, L, threshold):
    counter = list()
    Level = list()
    for a in L:
        count = 0
        items = a.split(DELIMITER)
        for bought in dataset:
            flag = True
            for i in range(len(items)):
                if items[i] not in bought:
                    flag = False
                    break
            if flag == True:
                count += 1
        if count >= threshold:
            counter.append(count)
            Level.append(a)
    return Level, counter


def has_frequent_subset(candidate, L):
    toBeDeleted = list()
    for elements in candidate:
        items = elements.split(DELIMITER)
        itemLen = len(items)
        flag = True
        for j in range(itemLen):
            subset = ""
            subsetLen = 0
            for k in range(itemLen):
                if j != k:
                	subset += items[k]
                	subsetLen += 1
                	if itemLen - 1 != subsetLen:
                		subset += DELIMITER
            if subset not in L:
                flag = False
                break

        if flag == False:
            toBeDeleted.append(elements)

    candidate = [values for values in candidate if values not in toBeDeleted]
    return candidate


def candidate_generator(L):
    candidate = set()
    length = len(L)

    for i in range(length):
        for j in range(i + 1, length):
            itemsI = L[i].split(DELIMITER)
            itemsJ = L[j].split(DELIMITER)
            flag = 1
            for x in range(len(itemsI) - 1):
                if itemsI[x] != itemsJ[x]:
                    flag = 0
            if flag:
                new = L[i] + DELIMITER + itemsJ[-1]
                candidate.add(new)

    return list(sorted(candidate))


def find_frequent_1_itemsets(dataset):
    level1 = set()
    for elements in dataset:
        items = elements.split(DELIMITER)
        for i in range(len(items)):
            level1.add(items[i])

    return list(sorted(level1))


def Print(Level, counter):
    for i in range(len(Level)):
        if not Level[i]:
            break
        print("Level %d: " % (i + 1))
        print(Level[i])
        print('========================================')
        for j in range(len(Level[i])):
            print("'{0}'\t\t" .format(Level[i][j]), counter[i][j])


def Input():
    ans = input("Want to find confidence? (y/n)\n")
    if ans == "y":
        given = input("Given? (Format: I1,I2)\n")
        conFor = input("Confidence For? (Format: I5)\n")
        return given, conFor
    else:
        print("==SPECIFIED ITEMS ARE INFREQUENT==")


def Confidence(Level, counter, given, conFor):
    givenList = given.split(DELIMITER)
    conForList = conFor.split(DELIMITER)

    conValueList = list()
    conValueList.extend(givenList)
    conValueList.extend(conForList)
    conValueList = sorted(conValueList)

    conValue = ""
    for i in range(len(conValueList)):
        conValue += conValueList[i]
        if i != len(conValueList) - 1:
            conValue += DELIMITER

    flagG, flagV = False, False
    countG, countV = 0, 0
    for i in range(len(Level)):
        if given in Level[i]:
            flagG = True
            countG = counter[i] [Level[i].index(given)]
        if conValue in Level[i]:
            flagV = True
            countV = counter[i] [Level[i].index(conValue)]

        if flagG and flagV:
            break

    if flagG and flagV:
        confidence = (countV / countG) * 100.0
        print("Confidence of {0} GIVEN {1} : {2:.2f}%" .format(
            conFor, given, float(confidence)))


if __name__ == '__main__':
    main()
