class Node:
	def __init__(self,data):
		self.next = None
		self.data = data



class LinkedList:
	def __init__(self):
		self.head = None


	def append_value(self,data):
		node = Node(data)
		if not self.head:
			self.head= node
			return 
		temp = self.head
		while temp.next:
			temp=temp.next
		temp.next = node

	def find_middle(self):
		if self.head ==None:
			return "No elements in the Linked List"

		frst_pointer = self.head
		second_pointer = self.head
		thrd_pointer = self.head
		while second_pointer and second_pointer.next:
			second_pointer = second_pointer.next.next
			thrd_pointer = frst_pointer
			frst_pointer = frst_pointer.next

		if frst_pointer:
			if len(lst)%2==0:
				return frst_pointer.data,thrd_pointer.data
			return frst_pointer.data
		return "couldn't find the middle"

lst = [1,2,3,22,31,12,12,42,312]
llm  = LinkedList()
for i in lst:
	llm.append_value(i)
print(llm.find_middle())