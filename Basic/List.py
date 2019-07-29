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

	#nested list, we can use list with in list

	list1=[[1,2,3],[4,5],[6,7]]

	print(list1[0][1])		#list1[0][1] => [1,2,3] => 2
	print(list1[1][1])		#list1[1][1] => [4,5] => 5

	############     list buildin functions    #################
	#add data at end of the list => append
	tmplist=list()			#make empty list
	tmplist.append(1)		#add 1 in tmplist
	tmplist.append('Hello')	#add 'Hello' in tmplist
	tmplist.append([2,3,4])	#add [2,3,4] in tmplist
	print(tmplist)			#output => [1,'Hello',[2,3,4]]


	#add data at specific position =>insert
	tmplist.insert(2,'World')		#insert 'World' at position 2
	tmplist.insert(-1,'Ronak')		#insert 'Ronak' at second last position

	#add another list at end => extend
	tmplist.extend(names)			#extend tmplist and add names at end

	#find index of element in list
	tmplist.index("World")			#return the index position of given element

	#delete last element and retrun the deleted element => pop
	tmplist.pop()					#delete the last element

	#delete element from list ( 1st instance only)
	tmplist.remove("Hello")

	#delete element from list with given index position
	tmplist.pop(2)					#delete 2nd element from list

	#sort the list
	tmplist.sort()

	#reverse the list
	tmplist.reverse()

	#count the occerence of element in list
	tmplist.count("Ronak")

	#copy a list without reference
	#with pointer
	a=[1,2,3]
	b=a 		#b is just point to a if we add element in a it also reflects b
	c=a.copy() 	#c is not pointer to a, changes in a doesn't reflect c





	#remove all elements => clear
	tmplist.clear()


	print(tmplist)			#output => [1,'Test']
if __name__ == '__main__':
	main()