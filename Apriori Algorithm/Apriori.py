def main():
	dataset = readFile()
	L1 = find_frequent_1_itemsets(dataset)
	ItemsetsLevel, ItemsetsCounter = apriori(dataset)
	Print(ItemsetsLevel, ItemsetsCounter)
	Confidence(ItemsetsLevel, ItemsetsCounter)



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
		Level, L_count = has_Minimum_Support_Counter(dataset, candidate, threshold)

		resultLevel.append(Level)
		resultCounter.append(L_count)


	return resultLevel, resultCounter


def has_Minimum_Support_Counter(dataset, L, threshold):
	counter = list()
	Level = list()
	for a in L:
		count = 0
		items = a.split(",")
		for bought in dataset:
			flag = True
			for i in range(len(items)):
				#print(items[i], bought)
				if items[i] not in bought:
					#print("not matched")
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
		#print(elements)
		items = elements.split(",")
		itemLen = len(items)
		flag = True
		for j in range(itemLen):
			subset = ""
			c = 1
			for k in range(itemLen):
				if j != k:
					if itemLen - 1 == c:
						subset += items[k]

					else:
						subset += items[k] + ","
						c += 1

			if subset not in L:
				flag = False
				break

		if flag == False:
			toBeDeleted.append(elements)

	candidate = [values for values in candidate if values not in toBeDeleted ]
	#print("Candidates after:", candidate)
	return candidate



def candidate_generator(L):
	candidate = set()
	length = len(L)

	for i in range(length):
		for j in range(i+1, length):
			itemsI = L[i].split(",")
			itemsJ = L[j].split(",")
			flag = 1
			for x in range(len(itemsI)-1):
				if itemsI[x] != itemsJ[x]:
					flag = 0

			if flag:
				new = L[i] + "," + itemsJ[-1]
				candidate.add(new)

	return list(sorted(candidate))



def find_frequent_1_itemsets(dataset):
	level1 = set()

	for elements in dataset:
		items = elements.split(",")

		for i in range(len(items)):
			level1.add( items[i] )

	return list(sorted(level1))



def Print(Level, counter):
	for i in range(len(Level)):
		if not Level[i]:
			break
		print("Level %d: " % (i+1))
		print(Level[i])
		print('========================================')
		for j in range(len(Level[i])):
			print("'{0}'\t\t" .format(Level[i][j]), counter[i][j])


def Confidence(Level, counter):
	ans = input("Want to find confidence? (y/n)\n")
	if ans == "y":
		given = input("Given? (Format: I1,I2)\n")
		conFor = input("Confidence for? (Format: I5)\n")

		print(given, conFor)



if __name__ == '__main__':
	main()