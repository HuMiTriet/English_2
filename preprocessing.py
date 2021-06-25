import math

def find_pattern(processed_path):
	result = ''
	last_char = len(processed_path)-1
	expand = 0
	last_pattern = ''
	next_pattern = ''
	while expand < math.floor(len(processed_path)/2):
		last_pattern = processed_path[last_char-expand] + last_pattern
		for i in range(len(last_pattern)):
			next_pattern = processed_path[last_char - expand -i -1 ] + next_pattern
		if next_pattern != last_pattern:
			next_pattern = ''
			expand += 1
		else:
			result = last_pattern
			return result

	 
	
def check_path_possible(processed_path,kripke_matrix):
	result = True
	for i in range(len(processed_path)):
		if i == (len(processed_path) -1):
			return result;
		if kripke_matrix[int(processed_path[i]),int(processed_path[i+1])] != 1:
			result = False
			return result;