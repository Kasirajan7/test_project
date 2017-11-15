class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        if len(self.stack):
            print("Non Empty list")
        else :
            print("Empty list")

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) ==0:
            print("Stack is empty")
            return
        else:
            print(self.stack.pop(-1))
            return
 
    def print(self):
        print("-------------")
        print(len(self.stack))
        if len(self.stack)==0:
            print("Empty stack")
        else:
            for i in range(len(self.stack)):
                print(self.stack[i])


stack=Stack()
stack.print()
stack.isEmpty()
stack.push(5)
stack.push(9)
stack.push(11)
stack.print()
stack.pop()
stack.print()
stack.isEmpty()
