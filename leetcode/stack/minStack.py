class MinStack:


    def __init__(self):
        self.stack=[]
        self.stack_min=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_min:
            self.stack_min.append(min(val,self.stack_min[-1]))
        else:
            self.stack_min.append(val)

            
        

    def pop(self) -> None:
        self.stack_min.pop()
        return self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        


    def getMin(self) -> int:
        return self.stack_min[-1]

        


minStack = MinStack()
minStack.push(2)
minStack.push(3)
minStack.push(4)
minStack.push(1)

print(minStack.pop())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())


print(minStack)



# stack =    2 3 4 1
# minStack = 2 2 2 1