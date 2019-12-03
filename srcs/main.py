from parse import Parser
import math
import os
import sys

USAGE = 'Usage : python3 main.py [file_location]'

def error(reason):
	exit(reason + USAGE)

def get_file():
	if len(sys.argv) == 1:
		 error('No arguments\n')
	elif len(sys.argv) > 2:
		error('Too many arguments!\n')
	os.getcwd()
	filename = sys.argv[1]
	file = open(filename, "r")
	return file

def main():
	file = get_file()
	Parser.parsing(file)
	file.close()

if __name__ == '__main__':
	main()