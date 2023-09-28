class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop() # right end element of output

    def peek(self) -> int:
        if not self.output: # if output is empty
            while self.input: # append input element in reverse order
                self.output.append(self.input.pop())
        return self.output[-1] # left end element of input

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
