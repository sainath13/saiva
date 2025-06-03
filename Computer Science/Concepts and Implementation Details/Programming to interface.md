```java

Set<Integer> set = new HashSet<>();
```

This is an example of **programming to an interface**, a common best practice in Java. It allows flexibility: you can later change `HashSet` to another implementation like `TreeSet` or `LinkedHashSet` without changing the rest of your code.

---

### Analogy:

Think of it like this:
- `Set` = contract (interface)
- `HashSet` = actual product that fulfills the contract (concrete class)