def main():
	dataset = readFile()
	#print(dataset)
	L1 = find_frequent_1_itemsets(dataset)
	L1Counter = SupportCounter(dataset, L1, 2)
	Itemsets = apriori(dataset, L1)


def SupportCounter(dataset, L, k):
	counter = list()
	for a in L:
		count = 0
		items = a.split(",")
		for bought in dataset:
			flag = True
			for i in range(len(items)):
				print(items[i], bought)
				if items[i] not in bought:
					print("not matched")
					flag = False
					break
			'''if [items[i] in bought for i in range(len(items))]:
				count += 1'''
			if flag == True:
				count += 1

		counter.append(count)
	print(counter)
	return counter




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
	

def apriori(dataset, L1):
	resultLevel = list()
	resultCounter = list()
	#L = find_frequent_1_itemsets(dataset)
	#print(L)

	L = L1
	print("L: "+L)
	#while L:
	candidate = candidate_gen(L)
	print(candidate)


	return result


def candidate_gen(L):
	candidate = set()
	#print(L)

	'''length = len(L)
	print(length)
	for i in range(length):
		for j in range(i+1, length):
			itemsI = L[i].split(",")
			itemsJ = L[j].split(",")
			#print(itemsI[-1], itemsJ[-1])

			if itemsI[-1] < itemsJ[-1] and [itemsI[x] == itemsJ[x] for x in range(len(itemsI)-1)]:
				new = L[i] + "," + itemsJ[-1]
				print(new)
				candidate.add(new)
				#if has_infrequent_subset(new, L):
					#del candidate[-1]'''

	length = len(L)
	for i in range(length):
		for j in range(i+1, length):
			#new = L[i]|L[j]
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
		print(len(items))
		for i in range(len(items)):
			level1.add( items[i] )

	#print(level1)
	return list(sorted(level1))



if __name__ == '__main__':
	main()