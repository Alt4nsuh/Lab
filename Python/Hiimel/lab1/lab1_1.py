class Stack:
    def __init__(self):
        self._list = []
    
    def push(self, element):
        self._list.append(element)

    def pop(self):
        self._list.pop()

    def peek(self):
        if not self.is_empty():
            return self._list[-1]
    def top(self):
      return self._list[0]
    def __len__(self):
        return len(self._list)
    
    def is_empty(self):
        return len(self._list) == 0
    
    def __str__(self):
        return str(self._list)
stack = Stack() 
stack.push('A') 
stack.push('B') 
stack.push('C') 
print('stack:', stack)
print('stack.is_empty():', stack.is_empty())
print('stack.length():', stack.__len__()) 
print('stack.top():', stack.top()) 
print('stack.pop():', stack.pop()) 
print('stack:', stack)
