f = open('cmudict-en-us.dict')
content = f.readlines()	
outputFile = open("generated-aave-pronunciations.txt","w")
for index in range(0, len(content)):
	line = content[index]
	lineSplitBySpaces = line.strip().split(' ')
	targetWord = lineSplitBySpaces[0]
	pronunciation = lineSplitBySpaces[1:]
	changed = False
	updatedPronunciation = pronunciation
	numToAdd = 1
	if (targetWord.find('(') >= 0):
		numToAdd = int(targetWord[targetWord.find('(') + 1 : targetWord.find(')')]);
		targetWord = targetWord[0 : targetWord.find('(')]
   # change starting th to d
	if (pronunciation[0] == "DH"):
		updatedPronunciation[0] = "D"
		changed = True

	# change starting th to t
	if (pronunciation[0] == "TH"):
		updatedPronunciation[0] = "T"
		changed = True

	# change starting str to sr
	if (pronunciation[0] == "S" and pronunciation[1] == "T" and pronunciation[2] == "R"):
		del updatedPronunciation[1]
		changed = True

	#change ng to n
	for i in range(len(updatedPronunciation)):
		if updatedPronunciation[i] == "NG":
			updatedPronunciation[i] = "N"
			changed = True

	if (updatedPronunciation[-1] == "ER"):
		updatedPronunciation[-1] == "UH"
		changed = True

	if (len(updatedPronunciation) >= 2):
		if (updatedPronunciation[-2] == "S" and updatedPronunciation[-1] == "P"):
			del updatedPronunciation[-1]
			changed = True
		elif (updatedPronunciation[-2] == "S" and updatedPronunciation[-1] == "T"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "S" and updatedPronunciation[-1] == "K"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "F" and updatedPronunciation[-1] == "T"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "P" and updatedPronunciation[-1] == "T"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "N" and updatedPronunciation[-1] == "D"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "S" and updatedPronunciation[-1] == "T"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "L" and updatedPronunciation[-1] == "D"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "R" and updatedPronunciation[-1] == "B"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "R" and updatedPronunciation[-1] == "D"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "ER" and updatedPronunciation[-1] == "D"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "UH" and updatedPronunciation[-1] == "R"):
			del updatedPronunciation[-1]
			changed = True 
		elif (updatedPronunciation[-2] == "AO" and updatedPronunciation[-1] == "R"):
			del updatedPronunciation[-1]
			changed = True 

	if (changed):
		existingPronunciations = 1
		if (content[index+4-numToAdd].strip().split(' ')[0].find('(4') >= 0):
			existingPronunciations = 4
		elif (content[index+3-numToAdd].strip().split(' ')[0].find('(3') >= 0):
			existingPronunciations = 3
		elif (content[index+2-numToAdd].strip().split(' ')[0].find('(2') >= 0):
			existingPronunciations = 2
		newPronunciationNumber = numToAdd + existingPronunciations
		outputFile.write(targetWord + "(" + str(newPronunciationNumber) + ") " + ' '.join(map(str,updatedPronunciation)) + "\n")

outputFile.close()
