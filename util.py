import sys
import inspect
import heapq

class Stack:
  
    def __init__(self):
        self.list = []

    def push(self,item):
       
        self.list.append(item)

    def pop(self):
     
        return self.list.pop()

    def isEmpty(self):
      
        return len(self.list) == 0

class Queue:
  
    def __init__(self):
        self.list = []

    def push(self,item):
      
        self.list.insert(0,item)

    def pop(self):
      
        return self.list.pop()

    def isEmpty(self):
      
        return len(self.list) == 0

class PriorityQueue:
   
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
      
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class PriorityQueueWithFunction(PriorityQueue):
  
    def  __init__(self, priorityFunction):
      
        self.priorityFunction = priorityFunction      
        PriorityQueue.__init__(self)       

    def push(self, item):
        
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance( xy1, xy2 ):
 
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )



def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)

