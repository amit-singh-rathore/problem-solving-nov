class MaxHeap:
	def __init__(self, heap=[0]):
		if heap:
			self.heap = [0]
			for item in heap:
				self.heap.append(item)
				self.__floatup(len(self.heap) - 1)
		else:
			self.heap = heap
	
	def __len__(self):
		return len(self.heap)
	
	def __repr__(self):
		return f"{self.__class__.__name__}({self.heap})"
	
	def push(self, item):
		self.heap.append(item)
		self.__floatup(len(self.heap) - 1)
	
	def peek(self):
		if len(self) > 1:
			return self.heap[1]
	
	def pop(self):
		if len(self) == 2:
			max_val = self.heap.pop()
		elif len(self) > 2:
			self.__swap(1, len(self.heap) - 1)
			max_val = self.heap.pop()
			self.__bubbledown(1)

		return max_val
		
	def __get_left_child(self, idx):
		left_child_idx = idx * 2
		return self.heap[left_child_idx]
	
	def __get_right_child(self, idx):
		right_child_idx = idx * 2 + 1
		return self.heap[right_child_idx]
	
	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	
	def __floatup(self, idx):
		if idx <= 1:
			return
		
		parent_idx = idx // 2
		if self.heap[parent_idx] < self.heap[idx]:
			self.__swap(parent_idx, idx)
			self.__floatup(parent_idx)
	
	def __bubbledown(self, idx):
		left_child_idx = idx * 2
		right_child_idx = left_child_idx + 1

		largest_idx = idx
		if len(self) > left_child_idx and self.heap[largest_idx] < self.heap[left_child_idx]:
			largest_idx = left_child_idx

		if len(self) > right_child_idx and self.heap[largest_idx] < self.heap[right_child_idx]:
			largest_idx = right_child_idx

		if largest_idx != idx:
			self.__swap(idx, largest_idx)
			self.__bubbledown(largest_idx)