class LinearQueue():
    def __init__(self, size):
        self.size = size
        self.front = self.rear = -1
        self.container = [None]*size
        print(f"Initializd a queue with the given size {size}")

    def is_full(self):
        if self.rear+1 == self.size:
            print("The queue is full.")
            return True
        return False

    def is_empty(self):
        if self.front == self.rear == -1:
            print("The queue is empty.")
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            print(f"Can not put the item {item} to the queue.")
            return

        if self.is_empty():
            self.front += 1

        self.rear += 1
        self.container[self.rear] = item
        print(f"Put the item {item} to the queue with index {self.rear}.")
        return

    def dequeue(self):
        if self.is_empty():
            print("There is no more item that can be taken.")
            return

        item = self.container[self.front]
        self.container[self.front] = None
        print(f"Get the item {item} from the queue with index {self.front}.")
        self.front += 1
        return item


if __name__ == "__main__":
    queue = LinearQueue(5)
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
    queue.enqueue(5)

    print("End of story.")
