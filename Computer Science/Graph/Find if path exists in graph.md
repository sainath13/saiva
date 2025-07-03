### Depth First Search (DFS): Recursive

```java
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        boolean[] seen = new boolean[n];

        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            graph.computeIfAbsent(a, val -> new ArrayList<>()).add(b);
            graph.computeIfAbsent(b, val -> new ArrayList<>()).add(a);
        }

        return dfs(graph, seen, source, destination);
    }
    
    private boolean dfs(Map<Integer, List<Integer>> graph, boolean[] seen, int currNode, int destination) {
        if (currNode == destination) {
            return true;
        }
        seen[currNode] = true;
        for (int nextNode : graph.get(currNode)) {
            if (!seen[nextNode]) {  // Only call dfs if not seen
                if (dfs(graph, seen, nextNode, destination)) {
                    return true;
                }
            }
        }
        return false;
    }
}

```

#### Complexity Analysis

Let n be the number of nodes and m be the number of edges.

- Time complexity: O(n+m)
    
    - In a typical BFS search, the time complexity is O(V+E) where V is the number of vertices and E is the number of edges. There are n nodes and m edges in this problem.
        - We build adjacent list of all `m` edges in `graph` which takes O(m).
        - Each node is added to the queue and popped from queue once, it takes O(n) to handle all nodes.
    - The time complexity is O(n+m).
- Space complexity: O(n+m)
    
    - We used a hash map `neighbors` to store all edges, which requires O(m) space for m edges.
    - We use `seen`, either a hash set or an array to record the visited nodes, which takes O(n) space.
    - There may be up to n nodes stored in `queue` and O(n) space is required.
    - Therefore, the space complexity is O(n+m).


### Depth First Search (DFS): Iterative
```java
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        // Store all edges according to nodes in 'graph'.
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            graph.computeIfAbsent(a, val -> new ArrayList<Integer>()).add(b);
            graph.computeIfAbsent(b, val -> new ArrayList<Integer>()).add(a);
        }
        
        // Start from source node, add it to stack.
        boolean[] seen = new boolean[n];
        seen[source] = true;
        Stack<Integer> stack = new Stack<>();
        stack.push(source);
        
        while (!stack.isEmpty()) {
            int currNode = stack.pop();
            if (currNode == destination) {
                return true;
            }
            // Add all unvisited neighbors of the current node to stack'
            // and mark it as visited.
            for (int nextNode : graph.get(currNode)) {
                if (!seen[nextNode]) {
                    seen[nextNode] = true;
                    stack.push(nextNode);
                }
            }
        }
        
        return false; 
    }
}
```

#### Complexity Analysis

Let n be the number of nodes and m be the number of edges.

- Time complexity: O(n+m)
    
    - In a typical DFS search, the time complexity is O(V+E) where V,E is the number of vertices and edges. In this problem, there are n nodes and m edges:
        - We build adjacent list of all `m` edges in `graph` which takes O(m).
        - Each node is added to the stack and popped from stack once, it takes O(n) to handle all nodes.
    - Therefore, the time complexity is O(n+m).
- Space complexity: O(n+m)
    
    - We use a hash map to store `m` edges, it takes O(m) space.
    - We use one bool array `seen` to record visited nodes, which also takes O(n) space.
    - We use a stack `stack` to store all nodes to be visited, in the worst-case scenario, there may be O(n) nodes in `stack`.
    - To sum up, the space complexity is O(n+m).




### Breadth First Search (BFS)
```java
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        //Store all edges in 'graph'.
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            graph.computeIfAbsent(a, val -> new ArrayList<Integer>()).add(b);
            graph.computeIfAbsent(b, val -> new ArrayList<Integer>()).add(a);
        }
        
        // Store all the nodes to be visited in 'queue'.
        boolean[] seen = new boolean[n];
        seen[source] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(source);
        
        while (!queue.isEmpty()) {
            int currNode = queue.poll();
            if (currNode == destination) {
                return true; 
            }

            // For all the neighbors of the current node, if we haven't visit it before,            
            // add it to 'queue' and mark it as visited.
            for (int nextNode : graph.get(currNode)) {
                if (!seen[nextNode]) {
                    seen[nextNode] = true;
                    queue.offer(nextNode);
                }
            }
        }
        
        return false;
    }
}
```

#### #### Complexity Analysis

Let n be the number of nodes and m be the number of edges.

- Time complexity: O(n+m)
    
    - In a typical BFS search, the time complexity is O(V+E) where V is the number of vertices and E is the number of edges. There are n nodes and m edges in this problem.
        - We build adjacent list of all `m` edges in `graph` which takes O(m).
        - Each node is added to the queue and popped from queue once, it takes O(n) to handle all nodes.
    - The time complexity is O(n+m).
- Space complexity: O(n+m)
    
    - We used a hash map `neighbors` to store all edges, which requires O(m) space for m edges.
    - We use `seen`, either a hash set or an array to record the visited nodes, which takes O(n) space.
    - There may be up to n nodes stored in `queue` and O(n) space is required.
    - Therefore, the space complexity is O(n+m).



###  Disjoint Set Union (DSU)
```java
class UnionFind {
    private int[] root;
    private int[] rank;
    public UnionFind(int n) {
        this.root = new int[n];
        this.rank = new int[n];
        for (int i = 0; i < n; ++i) {
            this.root[i] = i;
            this.rank[i] = 1;
        }
    }   
    public int find(int x) {
        if (this.root[x] != x) {
            this.root[x] = find(this.root[x]);
        }
        return this.root[x];
    }
    public void union(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            if (this.rank[rootX] > this.rank[rootY]) {
                int tmp = rootX;
                rootX = rootY;
                rootY = tmp;
            }
            // Modify the root of the smaller group as the root of the
            // larger group, also increment the size of the larger group.
            this.root[rootX] = rootY;
            this.rank[rootY] += this.rank[rootX];
        }
    }
}

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        UnionFind uf = new UnionFind(n);

        for (int[] edge : edges) {
            uf.union(edge[0], edge[1]);
        }

        return uf.find(source) == uf.find(destination);
    }
}
```

##### Complexity Analysis

Let n be the number of nodes and m be the number of edges.

- Time complexity: O(m⋅α(n))
    
    - The amortized complexity for performing m union find operations is O(m⋅α(n)) time where α is the [Inverse Ackermann Function](https://en.wikipedia.org/wiki/Ackermann_function#Inverse).
    - To sum up, the overall time complexity is O(m⋅α(n)).
- Space complexity: O(n)
    
    - We used two arrays `root` and `rank` to save the root and rank of each node in the DSU data structure, each of them takes O(n) space.
    - To sum up, the overall time complexity is O(n).