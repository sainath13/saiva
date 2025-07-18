- processes the data in order means elements are inserted at the end and removed from the front
```java

Queue<Obj> queue = new LinkedList<Obj>();

Queue<String> pq = new PriorityQueue<>();

pq.add("Geeks");
pq.add("For");
pq.add("Geeks");

Iterator iterator = pq.iterator();

while (iterator.hasNext()) {
    System.out.print(iterator.next() + " ");
}

```



- ****add(element)****: 
	Adds an element to the rear of the queue. 
	If the queue is full, it throws an exception.
- ****offer(element):**** 
	Adds an element to the rear of the queue. 
	If the queue is full, it returns false.
- ****remove()****: 
	Removes and returns the element at the front of the queue. 
	If the queue is empty, it throws an exception.
- ****poll():**** 
	Removes and returns the element at the front of the queue. 
	If the queue is empty, it returns null.
- ****element():**** 
	Returns the element at the front of the queue without removing it. 
	If the queue is empty, it throws an exception.
- ****peek()****: 
	Returns the element at the front of the queue without removing it. 
	If the queue is empty, it returns null.


### Classes that implement the Queue Interface
1. PriorityQueue --> least element at the top
2. LinkedList
3. PriorityBlockingQueue --> thread safe priority queue




![[Pasted image 20250626114207.png]]