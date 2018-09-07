# create an array with all the dictionary words
# for each of the transcripts:
	# loop through each word and check if it's in the dictionary (binary search)
	# if word is NOT in dictionary, write to file of OODW for that transcript

def findWord(word, dictionary):
	if (len(dictionary) == 0):
		return 0
	else:
		middle = len(dictionary) // 2
		if (dictionary[middle] == word):
			return 1
		elif (dictionary[middle] > word):
			return findWord(word, dictionary[:middle])
		else:
			return findWord(word, dictionary[(middle+1):])

dictionary = [];
filepath = 'cmudict-en-us.dict'  
with open(filepath) as fp:  
	line = fp.readline()
	while line:
   		dictionary.append(line.split()[0])
   		line = fp.readline()

def findOOD(i, prefix):
	filepath = prefix + str(i) + '-s.txt'
	with open(filepath) as fp:
		outputFile = open(prefix + str(i) + "-ood.txt","w")
		line = fp.readline()
		while line:
			for word in line.split():
				if word != "<s>" and word != "</s>" and findWord(word, dictionary) == 0:
					outputFile.write(word + "\n")
			line = fp.readline()
		outputFile.close()


for i in range(101, 144):
	findOOD(i, "./McN")

for i in [149, 150, 152, 153, 155, 156, 157, 158, 159, 161, 162, 164, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]:
	findOOD(i, "./McN")

for i in range(2109, 2119):
	findOOD(i, './McNP')

for i in [2102, 2103, 2104, 2106, 2107, 2120, 2121, 2124, 2125, 2126, 2128, 2129]:
	findOOD(i, './McNP')

for i in range(2133, 2143):
	findOOD(i, './McNP')

for i in range(2144, 2153):
	findOOD(i, './McNP')

for i in range(2154, 2160):
	findOOD(i, './McNP')

for i in range(2161, 2182):
	findOOD(i, './McNP')
