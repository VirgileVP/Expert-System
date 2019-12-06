import main

# is_space:
# check if the char is a space, a tab or a line-return
def is_space(char):
	if char == ' ' or char == '\n' or char == '\t':
		return 1
	return 0


# check_parentheses:
# check and analyze stuff in parenthese
def check_parentheses(line, index):
	# TO DEVELOP
	return 1

# is_operator:
# check if it is a valid operator (+, |, =>, <=>, ^)
def is_operator(line, index):
	if line[index] == '(':
		check_parentheses(line, index) # not yet dev
	if line[index] == '+' or line[index] == '|' or line[index] == '^':
		return 1
	if line[index] == '=' and line[index + 1] == '>':
		return 1
	if line[index] == '<' and line[index + 1] == '=' and line[index + 2] == '>':
		return 1
	return 0

# is_fact:
# check if the char is a valid fact (only one letter, with or whitout '!' before)
def is_fact(line, index):
	if line[index] == '!':
		if line[index + 1].isalpha() == 1:
			return 1
		main.error("Facts must be letter\n", 0)
		return 0
	if line[index].isalpha() == 1:
		return 1
	main.error("Facts must be letter\n", 0)
	return 0

# is_rules:
# check if the line is a valid rules
def is_rules(line):
	i = 0
	while is_space(line[i]):
		i += 1
	if line[i] == '#':
		return 0
	if is_fact(line, i) == 0:
		return 0
	#if is_operator(line, i) == 1:

	else :
		error("Invalid operator or no operator\n", 0)
	return 1

# parsing:
# read and check all lines, store it if they are valid
def parsing(file):
	line = file.readline().rstrip('\n\r')
	rules = {} #dictionaire
	while line.isspace() or is_comment:
		line = file.readline().rstrip('\n\r')
	line = file.readline().rstrip('\n\r')
	if is_rules(line) != 1:
		main.error("Rules first", 0)
	line = file.readline().rstrip('\n\r')
	while is_rules(line):
		line = line.split('#')
		rules[i] = line[0]
		i += 1
		line = file.readline().rstrip('\n\r')
	i = 0
	for line in file:
		if is_rules(line) == 1:
			rules[i] = line
		i += 1