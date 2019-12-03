class Parser:
	def is_space(char):
		if char == ' ' or char == '\n' or char == '\t':
			return 1
		return 0

	def is_rules(line):
		i = 0
		while self.is_space(line[i]):
			i += 1
		if line[i] == '#':
			return 0
		return 1

	def parsing(file):
		# ligne par ligne f = file.readline().rstrip('\n\r')
		rules = {} #dictionaire
		i = 0
		for line in file:
			if self.is_rules() == 1:
				rules[i] = line
			# print(rules[i])
			i += 1