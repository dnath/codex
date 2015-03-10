class Queue(object):
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, item):
        self.input_stack.append(item)

    def dequeue(self):
        if len(self.output_stack) == 0:
            while len(self.input_stack) > 0:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.output_stack) + len(self.input_stack)



q = Queue()
a = [1, 2, 4, 9, 0, 8, 7, 3, 3, 1, 3, 4]
for item in a:
    q.enqueue(item)
while len(q) > 0:
    print q.dequeue(),