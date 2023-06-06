'''

file1 = open('actions.txt', 'r')
Lines = file1.readlines()
  
prompts = []
prompts2 = []
prompt3 = []
for line in Lines:
    if 'prompt' in line:
    	new = line.split(':')
    	prompts.append([new[1]])


for j in prompts:
	for i in j:
		if 'farm' in i:
			prompts2.append(i)


for i in prompts2:
	if len(i) < 25:
		prompt3.append(i)


file1 = open('tasks3.txt', 'w')
file1.writelines(prompts2)
file1.close()








print(prompts)



for i in prompts2:
	print(i)


'''
items = []
file1 = open('items.txt', 'r')
Lines = file1.readlines()
  

for item in Lines:
	items.append('enchant a ' + item)



print(items)


file1 = open('tasks4.txt', 'w')
file1.writelines(items)
file1.close()


