import re
import preprocessing

path = ['0','2','0','1','1']

pattern, div_index = preprocessing.find_pattern(path)

list_pattern = list(pattern)
while len(path[div_index:]) < len(path[:div_index]):
	path += list_pattern

for i in range(2):
	path += list_pattern

# path += list_pattern

print(path)
print(path[div_index:])
print(path[:div_index])
print(div_index)