class Node:
	def __init__(self,data):
		self.next = None
		self.data = data

	def __del__(self):
		print("node is deleted",self.data)

class LinkedList:
	def __init__(self):
		self.head = None



	def append_value(self,data):
		node = Node(data)
		if self.head == None:
			self.head = node
			return
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = node

	def append_beginning(self,data):
		node = Node(data)
		if self.head == None:
			self.head= node
			return 
		node.next = self.head
		self.head = node

	def delete_middle_element(self):
		frst_pointer = self.head
		second_pointer = self.head
		temp = self.head

		while second_pointer.next:
			temp = frst_pointer
			frst_pointer = frst_pointer.next
			second_pointer = second_pointer.next.next
		temp.next = frst_pointer.next
		print(frst_pointer.data)
		print(second_pointer.data)

	def delete_from_front(self):
		front = self.head
		temp = front.next
		self.head = temp

	def delete_fron_end(self):
		second_last = self.head
		temp = self.head
		while temp.next:
			second_last = temp
			temp=temp.next
		second_last.next=None

	def print_list(self):
		temp = self.head
		while temp:
			print(f"{temp.data} ->",end="")
			temp=temp.next



lst = [1,2,213213,1,1,23,14]

ll = LinkedList()
for i in lst:
	ll.append_beginning(i)
# ll.delete_middle_element()
# ll.delete_from_front()
ll.delete_fron_end()
ll.print_list()


