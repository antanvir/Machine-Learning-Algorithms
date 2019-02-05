def main():
	dataset = readFile()
	#print(dataset)
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
	result = list()
	L = find_frequent_1_itemsets(dataset)

	while L:
		candidate = candidate_gen(L)


	return result


def candidate_gen(L):
	candidate = set()

	length = len(L)
	for i in range(length):
		for j in range(length):
			itemsI = L[i].split(",")
			itemsJ = L[j].split(",")

			if [itemsI[-1] < itemsJ[-1] and itemsI[x] == itemsJ[x] for x in range(length-1)]:
				new = L[i] + "," + itemsJ[-1]
				print(new)
				candidate.add(new)
				#if has_infrequent_subset(new, L):
					#del candidate[-1]



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
	return list(level1)



if __name__ == '__main__':
	main()