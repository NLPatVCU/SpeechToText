import re

def replace(i, prefix):
	filepath = prefix + str(i) + '.txt'
	outputFile = open(prefix + str(i) + "-s.txt","w")
	with open(filepath) as fp:  
		line = fp.readline()
		count = 1
		while line:
			line = fp.readline()
			if (count > 2 and line.find(']') >= 0 and line.find("[pause]") < 0 and line.find("[end of audio]") < 0):
				text = "<s> " + line[line.find(']') + 4 : ].strip().lower()
				text = text.replace("?", "").replace("!", "").replace(".", "").replace("(", "").replace(")", "").replace(",", "")
				text = text.replace("xxxx", "").replace("youknow", "y'know").replace("=", "").replace("rr", "")
				text = re.sub(r"[a-z]xxx", "", text)
				text = text.replace("imean", "i mean").replace(":", "").replace('’',"'").replace("  ", " ")
				outputFile.write(text + " </s> \n")
			count += 1

for i in range(101, 144):
	replace(i, './McN')

for i in [149, 150, 152, 153, 155, 156, 157, 158, 159, 161, 162, 164, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]:
	replace(i, './McN')

for i in range(2109, 2119):
	replace(i, './McNP')

for i in [2102, 2103, 2104, 2106, 2107, 2120, 2121, 2124, 2125, 2126, 2128, 2129]:
	replace(i, './McNP')

for i in range(2133, 2143):
	replace(i, './McNP')

for i in range(2144, 2153):
	replace(i, './McNP')

for i in range(2154, 2160):
	replace(i, './McNP')

for i in range(2161, 2182):
	replace(i, './McNP')