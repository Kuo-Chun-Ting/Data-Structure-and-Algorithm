class CircularQueue():
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.container = [None]*size
        print(f"Initializd a queue with the given size {size}")

    def is_full(self):
        if (self.rear+1) % self.size == self.front:
            return True
        return False

    def is_empty(self):
        if self.front == self.rear == -1:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            print(f"Can not put the item {item} to the queue, the queue is full.")
            return

        if self.is_empty():
            self.front += 1

        self.rear = (self.rear+1) % self.size
        self.container[self.rear] = item
        print(f"Put the item {item} to the queue with index {self.rear}.")
        return

    def dequeue(self):
        if self.is_empty():
            print("There is no more item that can be taken, the queue is empty.")

        item = self.container[self.front]
        if item is None:
            return

        self.container[self.front] = None
        print(f"Get the item {item} from the queue with index {self.front}.")

        if self.container[(self.front+1) % self.size] == None:
            self.front = self.rear = -1
            return

        self.front = (self.front+1) % self.size
        return item


if __name__ == "__main__":
    queue = CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("End of story.")
