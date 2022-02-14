
class Stack():
    def __init__(self, size):
        self.top = -1
        self.container = [None]*size

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top+1 > len(self.container)-1:
            return True
        return False

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.container[self.top]
            print(f"Pushing {item} into the stack.")
        else:
            print("The stack is full.")

    def pop(self):
        if not self.is_empty():
            item = self.container[self.top]
            self.top -= 1
            print(f"Popping {item} out of the stack.")
            return item

        print("The stack is empty.")
        return None


if __name__ == '__main__':
    stack = Stack(5)
    
    print(stack.is_empty())
    print(stack.is_full())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
