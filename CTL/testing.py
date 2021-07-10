import numpy as np

kripke_matrix = np.array([	[0,1,1,0],
							[0,1,0,1],
							[1,0,0,1],
							[0,0,0,1] ])

# print(kripke_matrix)

labels = ['p','pq','pr','v']

formula = ['A','Xp']
# print(formula)

initial_states = []
initial_states.append(0)

# print(labels)
def Next_last():

def check_CTL(initial_states,formula,kripke_matrix):
	if formula[0] == 'A':
		final_result = True
		#since there is the case of the second TO has the AP attach to it we need to type case formula[1] into list
		list_TO_with_AP = list(formula[1])
		len_formula_1 = len(list_TO_with_AP)
		if list_TO_with_AP[0] == 'X' && len_formula_1 == 2:
			