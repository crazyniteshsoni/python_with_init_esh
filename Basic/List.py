def main():
	'''
	python list is collection of heterogeneous data elements.
	its like array in C but with mixed type of datatype can be
	used with in a list.'''

	a=[]			#make blank list
	b=list()		#initialize with list object => blank list

	#list with some initial values
	names=['john','mike','adolb','victor']
	numbers=[1,2,5,6,7,8]
	mixed=[1,'Shyam',15,58,90,'Ponjo',0.0,9.0]

	#access list element with index
	print(names[0])			# 0th element of names => 'john'
	print(numbers[-1])		# print last element of numbers => 8
	print(mixed[-2])		# print 2nd last element of mixed list => 0.0

	#for forward tracing list start with 0
	#for backward tracing list start with -1

	#access list elements with loop
	for i in range(len(names)):		#here len function is used for find length of list 
		print(names[i])

		#output => 'john' 'mike' 'adolb' 'victor'

	#iterate direct from list without index method
	for element in numbers:
		print(element)

		#output => 1 2 5 6 7 8

	

if __name__ == '__main__':
	main()