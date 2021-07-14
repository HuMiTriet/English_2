#comment is this language is the same as python # to start a new comment
#we first delete white space line and write a new file called code_p as the processed file
def preprocess(path):
	with open(path,'r') as code:
		for line in code:
			if line != '\n' and line[0] != '#':
				with open('./code_i.txt','a') as processed:
					processed.write(line)
				

#the resulting file will be name as code_i.txt