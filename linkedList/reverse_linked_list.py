class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def append_value(self,data):
		node= Node(data)
		if not self.head:
			self.head = node
			return 
		temp = self.head
		while 	temp.next:
			temp= temp.next
		temp.next = node
		# print(temp.data)

	def reverse_list(self):
		curr = self.head
		prev = None

		frst_element = self.head

		while curr:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node

		self.head = prev


	def print_list(self):
		temp = self.head
		while temp:
			print(f"{temp.data} -> ",end="")
			temp=temp.next



lst  = [1,2,21,2,131,3131,2431,1,2]

ll = LinkedList()
for i in lst:
	ll.append_value(i)

ll.reverse_list()
print(ll.print_list())