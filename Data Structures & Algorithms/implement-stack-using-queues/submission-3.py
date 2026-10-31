class MyStack:

    def __init__(self):
        self.q=deque()
        self.counter=0

    def push(self, x: int) -> None:
        self.q.append(x)
        return None
        
    def pop(self) -> int:
        if not len(self.q):
            return None
        n=1
        while self.q and n<len(self.q):
            cur=self.q.popleft()
            n+=1
            self.q.append(cur)
        return self.q.popleft()

    def top(self) -> int:
        if not len(self.q):
            return None
        n=0
        while self.q and n<len(self.q):
            cur=self.q.popleft()
            n+=1
            self.q.append(cur)
        return cur
        
    def empty(self) -> bool:
        return (not self.q)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()