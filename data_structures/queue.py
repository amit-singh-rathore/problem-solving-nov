class SingleEndedQueue:
	def __init__(self, queue=[]):
		self.queue = queue
		
	def __len__(self):
		return len(self.queue)
	
	def __repr__(self):
		return f"SingleEndedQueue({self.queue})"
	
	def enqueue(self, item):
		self.queue.insert(0, item)
	
	def dequeue(self):
		if len(self):
			return self.queue.pop()

	def clear(self):
		self.queue.clear()	
	