# this is an implementation of CTL using Python and Numpy
import numpy as np
import re

states = int(input("How many states: "))

#this is the matrix that will specify how our states can move between each others
kripke_matrix = np.zeros((states,states), dtype = np.int8 ) #initalize the matrix with all 0s

# print(kripke_matrix)

labels = []
type = ''
for s_it in range(states):
	raw_element = input("Input labels for s" + str(s_it) +  "(seperate each AP with a comma): ")
	processed_element = raw_element.split(',')
	for i in range(len(processed_element)):
		type  += processed_element[i]
	labels.append(type)
	type = ''

print(labels)

while True:
	raw_transition = input("Set transition (press e to stop): ")
	if raw_transition == 'e':
		break
	kripke_matrix[int(raw_transition[0]), int(raw_transition[2])] = 1

# print(kripke_matrix)

#what the following code does is that it substrings into smaller string by using regex, such that AXEGp -> A,X,E,Gp 
#the last capital letter will be stick to a lowercase character, it will tell our program to stop
raw_formula = input("enter CTL formula(No complex formula supported yet): ")
formula = []
formula = re.findall('[A-Z][^A-Z]*', raw_formula)

# print(formula)

#Since there is also the case of the NOT operator (N) we need to count how many Ns there are and flip the resut accordingly
NOT_counter = 0
while formula[0] == 'N':
	NOT_counter+=1
	formula.pop(0)

# print(formula)
# print(NOT_counter)

initial_states = []
input_state = int(input("Enter your starting states: "))
initial_states.append(input_state)

# print(initial_states)
# def check_CTL(initial_states,formula,kripke_matrix):
# 	if formula[0] == 'A':
# 		final_result = True
# 		#since there is the case of the second TO has the AP attach to it we need to type case formula[1] into list
# 		list_TO_with_AP = list(formula[1])
# 		len_formula_1 = len(list_TO_with_AP)
# 		if list_TO_with_AP[0] == 'X':
			


# while formula != []:

#REMEMBER THE FLIP THE RESULT #NOT_counter times