```java

PriorityQueue<Integer> heap = new PriorityQueue<>((n1,n2) -> map.get(n1) - map.get(n2));

```


The comparison `map.get(n1) - map.get(n2)` determines the order:
- If `map.get(n1)` is less than `map.get(n2)`, `n1` will come before `n2` in the heap.
- If `map.get(n1)` is greater than `map.get(n2)`, `n1` will come after `n2` in the heap.
- If the values are equal, their order in the heap is not defined (they could appear in any order).

```java
Map<Integer, Integer> map = new HashMap<>();
map.put(1, 5);
map.put(2, 3);
map.put(3, 8);
```

Then the priority queue will order the integers like this:
- 2 (because `map.get(2) = 3` is the smallest value),
- 1 (because `map.get(1) = 5`),
- 3 (because `map.get(3) = 8`).

When you call the `poll()` method on a `PriorityQueue` in Java, it removes and returns the **element with the highest priority**

- In a **max-heap**, the element with the **highest value** (or highest priority) is at the root.
- When you call `poll()`, it removes and returns the element with the highest priority (the largest value).


```java
(n1, n2) -> map.get(n1) - map.get(n2).   ===> MIN HEAP
```
- If `map.get(n1)` is less than `map.get(n2)`, `n1` will come before `n2`.
- This means the element with the **smallest mapped value** will be at the top of the heap.
- When popped smallest value will be popped 

```java
(n1, n2) -> map.get(n2) - map.get(n1).   ===> Max HEAP
```


------
So basically, (a,b) -> (a - b) This is min heap, We get min elements when we poll
(a,b) -> (b - a) This is max heap, We get max elements when we poll