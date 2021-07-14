# this is an implementation of LTL using Python and Numpy
import numpy as np
import re
import preprocessing
import TO

states = int(input("How many states: "))

#this is the matrix that will specify how our states can move between each others
kripke_matrix = np.zeros((states,states), dtype = np.int8 ) #initalize the matrix with all 0s

# print(kripke_matrix)

labels = []
type = ''
for s_it in range(states):
	raw_element = input("Input labels for s" + str(s_it) +  ": ")
	processed_element = raw_element.split(',')
	for i in range(len(processed_element)):
		type  += processed_element[i]
	labels.append(type)
	type = ''

while True:
	raw_transition = input("Set transition (press e to stop): ")
	if raw_transition == 'e':
		break
	kripke_matrix[int(raw_transition[0]), int(raw_transition[2])] = 1

# print(kripke_matrix)

raw_path = input("Enter your path: ")
processed_path = raw_path.split('-')

#pattern recognition: checking if the entered path has a repeating pattern at the end
pattern, div_index = preprocessing.find_pattern(processed_path)

while processed_path[0] != '0' or pattern == None:
	pattern = ''
	print("path must be started with the 0 state and ends with a pattern")
	raw_path = ''
	raw_path = input("Enter your path: ")
	processed_path = raw_path.split('-')
	pattern,div_index = preprocessing.find_pattern(processed_path)

#we need to balance the normal part and the pattern part
list_pattern = list(pattern)
while len(processed_path[div_index:]) < len(processed_path[:div_index]):
	processed_path += list_pattern

#add in two more patterns for good measure
for i in range(2):
	processed_path += list_pattern

# print(processed_path)
# print(div_index)

# getting the LTL formula
raw_formula = input("enter LTL formula: ")
print(raw_formula)
processed_formula = []
processed_formula = re.findall('[A-Z][^A-Z]*', raw_formula)

#the Regular expression above [A-Z][^A-Z]* split the uppercase latter into elements except for the last one with AP XGp -> X, Gp
# print(processed_formula)


if preprocessing.check_path_possible(processed_path,kripke_matrix) == False:
	print("NO, path not valid")
else:
	final_answer = bool

	#what iter of processed path are we on
	current_path = 0

	#we will not iterate through the LTL formula
	for formula_it in processed_formula:
		#we need to find what Teriary operator that we are dealing with:
		list_current_formula = list(formula_it)
		length  = len(list_current_formula)
		if list_current_formula[0] == 'X' and length ==1:
			current_path = TO.Next(current_path)
		if list_current_formula[0] == 'X' and length == 2:
			final_answer = TO.Next_last(length,current_path,processed_path,list_current_formula,labels)
		if list_current_formula[0] == 'X' and length == 1:
			current_path = TO.Next(div_index)
		if list_current_formula[0] == 'F' and length == 2:
			final_answer = TO.Future_last(current_path,processed_path,list_current_formula,labels)
		# current_path+=1
	# print(current_path)

	if final_answer == True:
		print("YES")
	else:
		print("NO")