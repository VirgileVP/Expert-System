import parse
import math
import os
import sys

USAGE = 'Usage : python3 main.py [file_location]'

# error:
# exit the programm with and error message
def error(reason, usage):
	if usage == 1:
		exit(reason + USAGE)
	exit(reason)

# get_file:
# check arguments and return the file
def get_file():
	if len(sys.argv) == 1:
		error('No arguments\n', 1)
	elif len(sys.argv) > 2:
		error('Too many arguments\n', 1)
	os.getcwd()
	filename = sys.argv[1]
	file = open(filename, "r")
	return file

def main():
	file = get_file()
	parse.parsing(file)
	file.close()

if __name__ == '__main__':
	main()