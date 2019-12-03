import math
import os
import sys

def error():
	exit

def main():
	if len(sys.argv) == 1:
		exit('There is no input arguments!' + '\n' + USAGE)
	elif len(sys.argv) > 2:
		exit('Too many arguments!' + '\n' + USAGE)

	filename = argv[1]
	os.getcwd()
	file = open("ressources/test1", "r")

	file.close()

if __name__ == '__main__':
	main()