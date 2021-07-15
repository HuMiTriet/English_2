import re
import os

print("This is a tiny language with commenting feature, start a comment with a #")
# path = input("Enter the path to your file: ")

path = "./code.txt"

file_name = re.findall('[^/]*[^.txt]',path)

file_name = file_name[-1]

print(file_name)

#comment is this language is the same as python # to start a new comment
#we first delete white space line and write a new file called code_p as the processed file
def preprocess(path):
	with open(path,'r') as code:
		for line in code:
			if line != '\n' and line[0] != '#':
				with open('./code_i.txt','a') as processed:
					processed.write(line)
				

#the resulting file will be name as code_i.txt

preprocess(path)

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

# deleting BEGIN and END in code_i.txt
with open('code_i.txt','r') as code:
	lines = code.readlines()
with open('code_i.txt','w')	as code:
	for single_line in lines:
			if single_line.strip('\n') != "BEGIN" and single_line.strip('\n') != "END":
				code.write(single_line)

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
			elif words[0] == "PRINT":
				words.pop(0)
				#we now check if print has the double "": ""	
				# print(words)
				#getting the first word and last word in words
				first_word = words[0]
				last_word = words[-1]
				# print(first_word)
				# print(last_word)	
				quotes_open = first_word[0:2]
				first_word = first_word.replace('"',"")
				quotes_close = last_word[-3:-1]
				last_word = last_word.replace('"',"")
				if quotes_open[0] == '"':
					if quotes_open == quotes_close:
						l_quotes_open = list(quotes_open)
						l_quotes_open[0] = '('
						first_word = l_quotes_open[0] + l_quotes_open[1] +first_word
						# print(first_word)
						l_quotes_close = list(quotes_close)
						l_quotes_close[1] = ')'
						last_word = last_word[:-1] + l_quotes_close[0] + l_quotes_close[1]
						# print(last_word)
						print_line = ""
						print_line += first_word
						for index_word in range(1,len(words) -1):
							print_line += " " + words[index_word]
						print_line+= " "
						print_line+= last_word
						print_line = "print"+print_line +'\n'
						# print(print_line)
						write_to_python(print_line,file_name)
					else:
						print("SYNTAX ERROR STRING FORMAT the closing quote has to match the opeing quote ")
				else:
					print("SYNTAX ERROR PRINT STATEMENT MUST START WITH A "" ")
			elif words[0] == "INPUT":
				words.pop(0)
				input_line =""
				variable = words[0]
				input_line += variable[:-1]
				input_line += " = input()\n"
				# print(input_line)
				write_to_python(input_line,file_name)

			else:
				print("SYNTAX ERROR ")
				break


os.remove("code_i.txt")