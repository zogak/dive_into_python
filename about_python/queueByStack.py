'''
stack 2개로 queue 구현하기
'''

# stack : first in, last out
# queue : first in, first out

class Queue:
    def __init__(self, stack1, stack2):
        self.stack1 = stack1
        self.stack2 = stack2

    def append(self, number):
        self.stack1.append(number)
        return self.stack1

    def pop(self):
        if len(self.stack2) == 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue([], [])
print(q.append(3))
print(q.append(4))
print(q.append(5))
print(q.pop())
print(q.pop())
print(q.pop())