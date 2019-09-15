import queue as queue

class Node:
    def __init__(self, x, y, parent):
        if(x < 0):
            x = 0
        if(y < 0):
            y = 0
        self.x = x
        self.y = y
        self.parent = parent
    def toString(self):
        return str(self.x) + "-" + str(self.y)

# Initial state is 0,0 and final state is either 0,d or d,0
# The problem is defined by a,b,d

a = int(input("Please enter the capacity of first bucket\n"))
b = int(input("Please enter the capacity of second bucket\n"))
d = int(input("Please enter the amount you need to measure\n"))


q = queue.Queue(maxsize=-1)
visited = {}

q.put(Node(0,0,None))
n = None
while not q.empty():
    n = q.get()
    if visited.__contains__(n.toString()):
        continue
    visited[n.toString()] = True
    if n.x == d and n.y == 0:
        break
    if n.x == 0 and n.y == d:
        break

    q.put(Node(0,n.y,n)) # Empty a
    q.put(Node(n.x,0,n)) # Empty b
    q.put(Node(a,n.y,n)) # Fill a
    q.put(Node(n.x,b,n)) # Fill b

    total = n.x + n.y

    # Transfer to b
    if total < b:
        q.put(Node(0,total,n))
    else:
        q.put(Node(total - b, b, n))

    if total < a:
        q.put(Node(total, 0, n))
    else:
        q.put(Node(a, total - a, n))


if n.x != d and n.y != d:
    print("Not Possible!")
else:
    stack = queue.LifoQueue(maxsize=-1)
    while n != None:
        stack.put(n)
        n = n.parent
    while stack.qsize() != 0:
        n = stack.get()
        print(n.toString())
        print("\n")
