![[Pasted image 20250626123337.png]]

## InOrder Traversal (Sorted order)
#### Recursive InOrder Traversal
```Java
  public static void printInorder(Node node) {
	if (node == null)
		return;
	// First recur on left subtree
	printInorder(node.left);
	// Now deal with the node
	System.out.print(node.data + " ");
	// Then recur on right subtree
	printInorder(node.right);
    }
```
#### Iterative InOrder Traversal
```java
    static ArrayList<Integer> inOrder(Node root) {
        ArrayList<Integer> ans = new ArrayList<>();
        Stack<Node> s = new Stack<>();
        Node curr = root;

        while (curr != null || !s.isEmpty()) {
            // Reach the left most Node of the curr Node
            while (curr != null) {
                // Place pointer to a tree node on
                // the stack before traversing
                // the node's left subtree
                s.push(curr);
                curr = curr.left;
            }
            // Current must be NULL at this point
            curr = s.pop();
            ans.add(curr.data);
            // we have visited the node and its
            // left subtree. Now, it's right
            // subtree's turn
            curr = curr.right;
        }
        return ans;
    }
```


## PreOrder Traversal
#### Recursive PreOrder
```Java
 public static void printPreorder(Node node) {
        if (node == null)
            return;
        // First deal with the node
        System.out.print(node.data + " ");
        // Then recur on left subtree
        printPreorder(node.left);
        // Finally recur on right subtree
        printPreorder(node.right);
    }
```

#### Iterative PreOrder
```Java
public static List<Integer> preOrder(Node root) {
        List<Integer> res = new ArrayList<>();
        if (root == null)
            return res;

        Stack<Node> s = new Stack<>();
        s.push(root);

        while (!s.isEmpty()) {
            Node curr = s.pop();
            res.add(curr.data);

            if (curr.right != null)
                s.push(curr.right);
            if (curr.left != null)
                s.push(curr.left);
        }

        return res;
    }
```


## PostOrder Traversal
#### Recursive PostOrder Traversal
```java
 void printPostorder(Node node) {
        if (node == null)
            return;
        // First recur on left subtree
        printPostorder(node.left);
        // Then recur on right subtree
        printPostorder(node.right);
        // Now deal with the node
        System.out.print(node.data + " ");
    }
```

#### Iterative PostOrder Traversal
##### Two Stack Iterative PostOrder Traversal
```Java
static ArrayList<Integer> postOrder(Node root) {
        ArrayList<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        // Create two stacks
        Stack<Node> stk1 = new Stack<>();
        Stack<Node> stk2 = new Stack<>();
        // Push root to first stack
        stk1.push(root);
        Node curr;
        // Run while first stack is not empty
        while (!stk1.isEmpty()) {
            // Pop from stk1 and push it to stk2
            curr = stk1.pop();
            stk2.push(curr);
            // Push left and right children of 
            // the popped node
            if (curr.left != null) {
                stk1.push(curr.left);
            }
            if (curr.right != null) {
                stk1.push(curr.right);
            }
        }
        // Collect all elements from second stack
        while (!stk2.isEmpty()) {
            curr = stk2.pop();
            result.add(curr.data);
        }
        return result;
    }
```

##### One Stack Iterative PostOrder Traversal
```java
static List<Integer> postOrder(Node root) {
        List<Integer> res = new ArrayList<>();
        Stack<Node> st = new Stack<>();
        while (true) {
            while (root != null) {
                st.push(root);
                st.push(root);
                root = root.left;
            }
            if (st.isEmpty())
                return res;
            root = st.pop();
            if (!st.isEmpty() && st.peek() == root)
                root = root.right;
            else {
                res.add(root.data);
                root = null;
            }
        }
    }

```