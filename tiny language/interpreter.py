import preprocessing

print("This is a tiny language with commenting feature, start a comment with a #")
path = input("Enter the path to your file: ")

preprocessing.preprocess(path)

program_start = False
program_end = False

#check if the program starts with BEGIN and end with END or not
with open('code_i.txt','r') as code:
	first_line = code.readline()
	for last_line in code:
		pass


if first_line == "BEGIN\n":
	program_start = True
else:
	print("Program does not have BEGIN")

if last_line == "END":
	program_end = True
else:
	print("program does not have END")

if program_start == True and program_end == True:
	print("CORRECT!!")

	print("Transalting to CPP file")

	
