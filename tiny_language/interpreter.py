import preprocessing
import re
import os

print("This is a tiny language with commenting feature, start a comment with a #")
# path = input("Enter the path to your file: ")

path = "./code.txt"

file_name = re.findall('[^/]*[^.txt]',path)

file_name = file_name[-1]

print(file_name)

preprocessing.preprocess(path)

program_start = False
program_end = False

#check if the program starts with BEGIN and end with END or not
with open('code_i.txt','r') as code:
	first_line = code.readline()
	for last_line in code:
		pass


if first_line == "BEGIN" or first_line == "BEGIN\n":
	program_start = True
else:
	print("Program does not have BEGIN")

if last_line == "END" or last_line == "END\n":
	program_end = True
else:
	print("program does not have END")

def write_to_python(line,file_name):
	with open(file_name+".py",'a') as final_file:
		final_file.write(line)

#starting the translation process
if program_start == True and program_end == True:
	print("CORRECT!!")

	print("Transalting to Python code file")
	with open('code_i.txt','r') as pseudo_py_code:
		for line in pseudo_py_code:
			words = list(line.split(' '))
			# print(words)
			if words[0] == "LET":
				words.pop(0)
				#we now need to convert the list back into a string
				# print(words)
				line = ""
				for ele in words:
					line += ele
				# print(line)
				write_to_python(line,file_name)
			# if words[0]


os.remove("code_i.txt")