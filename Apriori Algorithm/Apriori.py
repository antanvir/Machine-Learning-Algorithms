def main():
	dataset = readFile()
	#print(dataset)
	L1 = find_frequent_1_itemsets(dataset)
	#L1Counter = SupportCounter(dataset, L1, 2)
	Itemsets = apriori(dataset)






def readFile():
	file = open("transactions.txt", "r+")
	dataset = list()
	while True:
		line = file.readline().strip()
		#line = line.strip()
		item = line.split(" ")
		if not line:
			break
		#print(line)
		dataset.append(item[1])

	return dataset
	




def apriori(dataset):
	threshold = 2
	resultLevel = list()
	resultCounter = list()

	candidate = find_frequent_1_itemsets(dataset)
	Level, L_count = SupportCounter(dataset, candidate, threshold)
	print(L_count)
	print(Level)

	#while Level:
	candidate = candidate_gen(Level, 2)
	print(candidate)
	Level, L_count = SupportCounter(dataset, candidate, threshold)
	print(L_count)
	print(Level)



	return resultLevel, resultCounter


def SupportCounter(dataset, L, threshold):
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
	print(counter)
	return Level, counter





def candidate_gen(L, k):
	candidate = set()


	length = len(L)
	for i in range(length):
		for j in range(i+1, length):
			#new = L[i]|L[j]
			itemsI = L[i].split(",")
			itemsJ = L[j].split(",")
			if [itemsI[x] == itemsJ[x] for x in range(len(itemsI))]:
				new = L[i] + "," + L[j]
				candidate.add(new)

	return list(sorted(candidate))



def has_infrequent_subset(item, L):
	item = item.split(",")
	length = len(item)

	for i in range(length):
		for j in range(i+1, length):
			return True





def find_frequent_1_itemsets(dataset):
	level1 = set()

	for elements in dataset:
		items = elements.split(",")
		#print(len(items))
		for i in range(len(items)):
			level1.add( items[i] )

	#print(level1)
	return list(sorted(level1))



if __name__ == '__main__':
	main()