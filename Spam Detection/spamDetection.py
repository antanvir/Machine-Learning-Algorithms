from random import randrange, seed
from math import sqrt, ceil, log

spamMail, nonspamMail = 0, 0
pSpamWord = None
pNonspamWord = None

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
	# print(len(dataset), " ", len(dataset[1]))
	# print(dataset[1])
	return dataset


def trainData(dataset):
	
	for line in dataset:
		global spamMail, nonspamMail
		if(line[-1]) == 1.00:
			spamMail += 1
		else:
			nonspamMail += 1

	print(spamMail, "\t", nonspamMail)
	
	global pSpamWord, pNonspamWord
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
		
		pSpamWord[i] = (float(spamCount) + 1) / (spamCount + nonspamCount)			# NEED MODIFICATION
		pNonspamWord[i] = (float(nonspamCount) + 1) / (spamCount + nonspamCount)
		# print("spam + nonspam: "spamCount + nonspamCount)
	return pSpamWord, pNonspamWord


def crossValidation(dataset, pSpamWord, pNonspamWord):
	seed(10)
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
		accuracy += recentAccuracy

	accuracy /= 10
	print("Accuracy: ", accuracy, "%")


def checkTestset(test, pSpamWord, pNonspamWord):
	totalTestdata = len(test)
	correctlyClassified = 0

	for line in test:
		global spamMail, nonspamMail

		'''pSpam, pNonspam = 1, 1
		pSpam *= spamMail
		pNonspam *= nonspamMail
		'''
		pSpam, pNonspam = 0, 0
		pSpam += log((spamMail + 1) / (spamMail + nonspamMail))
		pNonspam += log((nonspamMail + 1) / (spamMail + nonspamMail))

		for i in range(len(line) - 1):			
			pSpam += log(pSpamWord[i])
			pNonspam += log(pNonspamWord[i])

		if pSpam > pNonspam and line[-1] == 1.00:
			correctlyClassified += 1
		elif pSpam < pNonspam and line[-1] == 0.00:
			correctlyClassified += 1

	recentAccuracy = (correctlyClassified * 100.0) / totalTestdata
	print('{0:0.2f} %'.format(recentAccuracy))

	return recentAccuracy



if __name__ == "__main__":
	main()