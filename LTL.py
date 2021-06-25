# this is an implementation of LTL using Python and Numpy
import numpy as np
import re
import preprocessing
import TO

states = int(input("How many states: "))

kripke_matrix = np.zeros((states,states), dtype = np.int8 )

print(kripke_matrix)

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

print(kripke_matrix)

raw_path = input("Enter your path: ")
processed_path = raw_path.split('-')

#pattern recognition:
pattern = preprocessing.find_pattern(processed_path)

while processed_path[0] != '0' or pattern == None:
	pattern = ''
	print("path must be started with the 0 state and ends with a pattern")
	raw_path = ''
	raw_path = input("Enter your path: ")
	processed_path = raw_path.split('-')
	pattern = preprocessing.find_pattern(processed_path)

#Since our pattern satisfy the condition we need to append the repeating pattern twice at the end
# print(pattern)


print(processed_path)

# getting the LTL formula
raw_ltl = input("enter LTL formula(for now doesn't support parenthesis must be typed explicitly): ")
print(raw_ltl)
processed_ltl = []
processed_ltl = re.findall('[A-Z][^A-Z]*', raw_ltl)

print(processed_ltl)


if preprocessing.check_path_possible(processed_path,kripke_matrix) == False:
	print("NO, path not valid")
else:
	# print("DUMMY TEXT")
	#first we need to find the AP in the LTL formula
	for formula_it in processed_ltl:
		check_1_2 = len(list(formula_it))
		if check_1_2 == 2:
			list_formula_it = list(formula_it)
			AP = list_formula_it[1]
			break
	
	final_answer = bool

	path_it = 0 # go through each element in our processed path (path, e.g., 0-2-0-1-1)
	current_state = 0 # to know which state we r currently on state s0)
	
	for i in range(len(processed_ltl)):
		

	if final_answer == True:
		print("YESSSSSS")
	elif final_answer == False:
		print("NOOOOOOO")

	# print(AP)



