import numpy as np       # numerical and scientific functions
import sys               # for access to command line arguments


# define a function that returns a value
def expo(x):
	return np.exp(x)   # numpy function e^x

#define a subroutine that does not return a variable
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))   # call the expo function

# define a main function
def main():
	
	n = 10   # provide a default value

	# check for command line arguments
	if(len(sys.argv)>1):
		n = int(sys.argv[1])   # if an arg exists set n to that

	show_expo(n)   # call the subroutine

# run the main function
if __name__ == "__main__":
	main()