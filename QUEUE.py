queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0
def enQueue(item):
 global queueLength, rearPointer
 if queueLength < queueFull:
  if rearPointer < len(queue) - 1:
   rearPointer = rearPointer + 1
  else:
   rearPointer = 0
  queueLength = queueLength + 1
  queue[rearPointer] = item
 else:
  print("Queue is full, cannot enqueue")
def deQueue():
 global queueLength, frontPointer, item
 if queueLength == 0:
  print("Queue is empty,cannot dequeue")
 else:
  item = queue[frontPointer]
  if frontPointer == len(queue) - 1:
   frontPointer = 0
  else:
   frontPointer = frontPointer + 1
 queueLength = queueLength -1
print(len(queue))

