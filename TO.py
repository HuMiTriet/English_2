#each functions will habve two modes either as a standalone TO, e.g., X, or as an TO with a AP,e.g., Xp

from numpy import true_divide

# def Future():
	

def Future_last(current_path,processed_path,list_current_formula,labels):
	result = bool
	remain_paths = len(processed_path) - current_path
	AP  = list_current_formula[1]
	for i in range(remain_paths):
		current_state = int(processed_path[current_path + i])
		AP_at_current_state = labels[current_state]
		list_AP_acs = list(AP_at_current_state)
		for i in list_AP_acs:
			if AP == i:
				result = True
				return result
			if AP != i:
				result = False
	return result



def Next(current_path):
	current_path +=1
	return current_path

def Next_last(current_path, processed_path,list_current_formula ,labels):
	result = bool
	#if len == 2 this is the end of the formula
	AP = list_current_formula[1]
	current_path += 1
	current_state = int(processed_path[current_path])
	AP_at_current_state = labels[current_state]
	list_AP_acs = list(AP_at_current_state)
	#for state that has more than 1 AP
	for i in list_AP_acs:
		if AP == i:
			result = True
			return result
		else:
			result = False
	return result