class DoubleEndedQueue:
	def __init__(self, queue = []):
		self.queue = queue
		
	def __len__(self):
		return len(self.queue)
	
	def __repr__(self):
		return f"{self.__class__.__name__}({self.queue})"
	
	def append(self, item):
		self.queue.append(item)
	
	def appendleft(self, item):
		self.queue.insert(0, item)
		
	def pop(self, item):
		if len(self):
			self.queue.pop()
	
	def popleft(self, item):
		if len(self):
			self.queue.pop(index=0)
			
	def clear(self):
		self.queue.clear()