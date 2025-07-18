```java

Stack<Integer> stack = new Stack<>();
// Default initialization of Stack
Stack stack1 = new Stack();

// Initialization of Stack
// using Generics
Stack<String> stack2 = new Stack<String>();
stack.push(1);
stack.push(2);
int x = stack.peek();  //See the top
int x = stack.pop();   //Remove the top

stack.isEmpty()

Integer pos = (Integer) stack.search(element);
if(pos == -1)
            System.out.println("Element not found");
        else
            System.out.println("Element is found at position: " + pos);

The Stack class in Java is inherits from [Vector in Java]
It is a thread-safe class. It is recommended to use [ArrayDeque].
For stack implementation as it is more efficient in a single-threaded environment.

 Deque<Character> stack = new ArrayDeque<Character>();
        stack.push('A');
        stack.push('B');
        
        System.out.println(stack.peek());
        System.out.println(stack.pop());

One more reason to use Deque over Stack is Deque has the ability to use streams convert to list with keeping LIFO concept applied while Stack does not.
-----------------------------------------------------------------------------
if we do this : push 1 then push 2
---------------------
List<Integer> list1 = stack.stream().collect(Collectors.toList());
Print list1 ===> 1, 2 --> LIFO is not maintained
---------------------
List<Integer> list1 = deque.stream().collect(Collectors.toList());
Print list1 ===> 2, 1 --> LIFO is maintained
----------------------------------------------------------------------------

```